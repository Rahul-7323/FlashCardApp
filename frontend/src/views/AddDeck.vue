<script>
import { useUserStore } from '@/stores/UserStore'

export default {
    setup() {
        const UserStore = useUserStore();
        return { UserStore }
    },
    data() {
        return {
            deck_name: ''
        }
    },
    methods: {
        async addDeck() {
            if(!this.deck_name){
                alert("Please enter a deck name");
                return false;
            }
            await this.UserStore.addDeck(this.deck_name);
            this.deck_name = '';
        }
    }
}

</script>

<template>
  <div>
    <div class="md:grid md:gap-6">
      
      <div class="mt-5 md:mt-0">
          <div class="shadow sm:rounded-md sm:overflow-hidden">
            <div class="px-4 py-5 bg-white space-y-6 sm:p-6">
              <div>
                <label for="deck-name" class="block text-sm font-medium text-gray-700"> Deck Name </label>
                <div class="mt-1">
                  <input v-model="deck_name" id="deck-name" name="deck-name" rows="3" class="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 mt-1 block w-full sm:text-sm border border-gray-300 rounded-md p-3" placeholder="Geography" />
                </div>
                <p class="mt-2 text-sm text-gray-500">The name of the deck</p>
              </div>
              
            </div>
            <div class="px-4 py-3 bg-gray-50 sm:px-6">
              <button @click="addDeck()" class="btn btn-primary py-0">Add Deck</button>
            </div>
          </div>
      </div>
    </div>
  </div>

  </template>
