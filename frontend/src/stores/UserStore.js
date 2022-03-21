import { defineStore } from 'pinia'
import { useAppStore } from '@/stores/AppStore'
import { useAuthStore } from '@/stores/AuthStore'

export const useUserStore = defineStore("UserStore", {
    state: () => {
        return {
            user: {},
            decks: [],
            cards: [],
            dataFetched: true,
        }
    },
    getters: {
        getCardsByDeckId: (state) => {
            return (deck_id) => state.cards.filter(card => card.deck_id == deck_id)
        },
    },
    actions: {
        async fetchData() {
            const AppStore = useAppStore();
            const AuthStore = useAuthStore();
            try {
                const data = await fetch(`http://localhost:5000/api/user_data/${AuthStore.userId}`, {
                                "method": "GET",
                                "headers": {
                                    "Authentication-Token": AuthStore.authenticationToken,
                                    "Content-Type": "application/json"
                                }
                                })
                    .then(resp => resp.json());
                console.log(data);
                this.user = data.user;
                this.decks = data.decks;
                this.cards = data.cards;
                AppStore.pushAlert({
                    type: 'success',
                    message: 'Successfully fetched the data from the API'
                });
            }
            catch {
                this.dataFetched = false;
                AppStore.pushAlert({
                    type: 'error',
                    message: 'Unable to fetch data from the API'
                });
            }
        },
        async addCard(deck_id, front, back){
            const AppStore = useAppStore();
            const AuthStore = useAuthStore();

            const data = {
                deck_id: deck_id,
                front: front,
                back: back,
                difficulty: null
            }

            await fetch("http://localhost:5000/api/card", {
                "method": "POST",
                "headers": {
                    "Authentication-Token": AuthStore.authenticationToken,
                    "Content-Type": "application/json"
                },
                "body": JSON.stringify(data)
            })
            .then(resp => {
                if(parseInt(resp.status) >= 400){
                    throw Error("Unable to add card");
                }
                return resp.json();
            })
            .then(data => {
                this.cards.push(data);
                AppStore.pushAlert({
                    type: 'info',
                    message: 'New card added'
                })
            })
            .catch(err => {
                AppStore.pushAlert({
                    type: 'error',
                    message: 'Unable to add card'
                })
                console.log(err);
            })

            
        },
        async addDeck(deck_name){
            const AppStore = useAppStore();
            const AuthStore = useAuthStore();

            const data = {
                user_id: this.user.id,
                deck_name: deck_name,
                last_review_time: new Date().toLocaleString(),
                total_score: 0
            }

            await fetch("http://localhost:5000/api/deck", {
                "method": "POST",
                "headers": {
                    "Authentication-Token": AuthStore.authenticationToken,
                    "Content-Type": "application/json"
                },
                "body": JSON.stringify(data)
            })
            .then(resp => {
                if(parseInt(resp.status) >= 400){
                    throw Error("Unable to add deck");
                }
                return resp.json();
            })
            .then(data => {
                this.decks.push(data);
                AppStore.pushAlert({
                    type: 'info',
                    message: 'New deck added'
                })
            })
            .catch(err => {
                AppStore.pushAlert({
                    type: 'error',
                    message: 'Unable to add deck'
                })
                console.log(err);
            })

            console.log(data);
        },
        async deleteCard(card_id){
            const AppStore = useAppStore();
            const AuthStore = useAuthStore();
        
            await fetch(`http://localhost:5000/api/card/${card_id}`, {
                    "method": "DELETE",
                    "headers": {
                        "Authentication-Token": AuthStore.authenticationToken,
                        "Content-Type": "application/json"
                    }
                    })
                .then(resp => {
                    if(parseInt(resp.status) >= 400){
                        throw Error("Unable to delete card");
                    }
                    return resp.json();
                })
                .then(data => {
                    for(let i=0; i<this.cards.length; i++){
                        if(this.cards[i].card_id == card_id){
                            this.cards.splice(i,1);
                            i--;
                        }
                    }
                    AppStore.pushAlert({
                        type: 'info',
                        message: `Deleted the card with card_id ${card_id}`
                    })
                })
                .catch(err => {
                    AppStore.pushAlert({
                        type: 'error',
                        message: 'Unable to delete card'
                    })
                console.error(err);
                });
        },
        async deleteDeck(deck_id){
            const AppStore = useAppStore();
            const AuthStore = useAuthStore();
        
            await fetch(`http://localhost:5000/api/deck/${deck_id}`, {
                    "method": "DELETE",
                    "headers": {
                        "Authentication-Token": AuthStore.authenticationToken,
                        "Content-Type": "application/json"
                    }
                    })
                .then(resp => {
                    if(parseInt(resp.status) >= 400){
                        throw Error("Unable to delete deck");
                    }
                    return resp.json();
                })
                .then(data => {
                    for(let i=0; i<this.decks.length; i++){
                        if(this.decks[i].deck_id == deck_id){
                            this.decks.splice(i,1);
                            i--;
                        }
                    }
                    for(let i=0; i<this.cards.length; i++){
                        if(this.cards[i].deck_id == deck_id){
                            this.cards.splice(i,1);
                            i--;
                        }
                    }
                    AppStore.pushAlert({
                        type: 'info',
                        message: `Deleted the deck with deck_id ${deck_id}`
                    })
                })
                .catch(err => {
                    AppStore.pushAlert({
                        type: 'error',
                        message: 'Unable to delete deck'
                    })
                console.error(err);
                });
        }
    }
})