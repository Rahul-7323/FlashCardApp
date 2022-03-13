import { defineStore } from 'pinia'
import { useAppStore } from '@/stores/AppStore'

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
            try {
                const data = await fetch("http://localhost:5000/api/user_data/2")
                    .then(resp => resp.json());
                console.log(data);
                this.user = data.user;
                this.decks = data.decks;
                this.cards = data.cards;
                AppStore.pushAlert({
                    type: 'success',
                    message: 'Successfully fetched the data from the API!'
                });
            }
            catch {
                this.dataFetched = false;
                AppStore.pushAlert({
                    type: 'error',
                    message: 'Unable to fetch data from the API!'
                });
            }
        },
    }
})