<script>
import { useUserStore } from '@/stores/UserStore';

export default {
    setup() {
      const UserStore = useUserStore();
      return { UserStore }
    },
    props: {
        deck: {
            default: {}
        }
    },
    computed: {
      numberOfCards() {
        return this.UserStore.getCardsByDeckId(this.deck.deck_id).length;
      }
    }
}
</script>

<template>
<div class="card bg-base-100 cool-shadow">
  <div class="card-body p-5">
    <h2 class="card-title">{{ deck.deck_name }}</h2>
    <div class="px-1 py-1 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
      <dt class="text-sm font-medium">No. of Cards</dt>
      <dd class="mt-1 text-sm sm:mt-0 sm:col-span-2">{{ numberOfCards }}</dd>
    </div>
    <div class="px-1 py-1 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
      <dt class="text-sm font-medium">Total Score</dt>
      <dd class="mt-1 text-sm sm:mt-0 sm:col-span-2">{{ deck.total_score }}</dd>
    </div>
    <div class="card-actions justify-center">
      <router-link :to="'/decks/'+deck.deck_id" class="btn btn-xs btn-primary">Cards</router-link>
      <button class="btn btn-xs btn-info">Review</button>
      <button class="btn btn-xs btn-error" @click="UserStore.deleteDeck(deck.deck_id)">Delete</button>
    </div>
  </div>
</div>
</template>