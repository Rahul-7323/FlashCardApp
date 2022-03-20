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
            return (deck_id) => state.decks.filter(deck => deck.deck_id === deck_id)
        }
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
                .then(resp => resp.json())
                .then(data => {
                    for(let i=0; i<this.decks.length; i++){
                        if(this.decks[i].deck_id == deck_id){
                            this.decks.splice(i,1);
                            i--;
                        }
                    }
                    AppStore.pushAlert({
                        type: 'info',
                        message: `Deleted the deck with deck_id ${deck_id}`
                    })
                })
                .catch(err => {
                console.error(err);
                });

        }
    }
})