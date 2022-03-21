<script>
import { useUserStore } from '@/stores/UserStore'

export default {
    setup() {
        const UserStore = useUserStore();
        return { UserStore }
    },
    data() {
        return {
            deck_id: null,
            front: '',
            back: ''
        }
    },
    computed: {
        decks() {
            return this.UserStore.decks;
        }
    },
    methods: {
        async addCard() {
            if(!this.deck_id){
                alert("Please select a deck");
                return false;
            }
            if(!this.front){
                alert("Please enter something for front");
                return false;
            }
            if(!this.back){
                alert("Please enter something for back");
                return false;
            }
            await this.UserStore.addCard(this.deck_id,this.front,this.back);
            this.deck_id = null;
            this.front = '';
            this.back = '';
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
                <div class="col-span-6 sm:col-span-3">
                  <label for="deck-name" class="block text-sm font-medium text-gray-700">Deck Name</label>
                  <select v-model="deck_id" id="deck-name" name="deck-name" class="mt-1 block w-full py-2 px-3 border border-gray-300 bg-white rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
                    <option v-for="deck in decks" :value="deck.deck_id">{{ deck.deck_name }}</option>
                  </select>
                </div>
              <div>
                <label for="front" class="block text-sm font-medium text-gray-700"> Front </label>
                <div class="mt-1">
                  <textarea v-model="front" id="front" name="front" rows="3" class="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 mt-1 block w-full sm:text-sm border border-gray-300 rounded-md p-3" placeholder="What is the powerhouse of the cell?" />
                </div>
                <p class="mt-2 text-sm text-gray-500">The front portion of a flash card usually contains a question or a word in a different language</p>
              </div>
              <div>
                <label for="back" class="block text-sm font-medium text-gray-700"> Back </label>
                <div class="mt-1">
                  <textarea v-model="back" id="back" name="back" rows="3" class="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 mt-1 block w-full sm:text-sm border border-gray-300 rounded-md p-3" placeholder="Mitochondria" />
                </div>
                <p class="mt-2 text-sm text-gray-500">The back portion contains the answer to the question in the front</p>
              </div>
            </div>
            <div class="px-4 py-3 bg-gray-50 sm:px-6">
              <button @click="addCard()" class="btn btn-primary py-0">Add Card</button>
            </div>
          </div>
      </div>
    </div>
  </div>

  </template>
