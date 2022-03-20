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
    }
}
</script>

<template>
<div class="card bg-base-100 cool-shadow">
  <div class="card-body p-5">
    <h2 class="card-title">{{ deck.deck_name }}</h2>
    <div class="px-1 py-1 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
      <dt class="text-sm font-medium">Last Review Time</dt>
      <dd class="mt-1 text-sm sm:mt-0 sm:col-span-2">{{ deck.last_review_time }}</dd>
    </div>
    <div class="px-1 py-1 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
      <dt class="text-sm font-medium">Total Score</dt>
      <dd class="mt-1 text-sm sm:mt-0 sm:col-span-2">{{ deck.total_score }}</dd>
    </div>
    <div class="card-actions justify-center">
      <button class="btn btn-xs btn-primary">Cards</button>
      <button class="btn btn-xs btn-info">Review</button>
      <button class="btn btn-xs btn-error" @click="UserStore.deleteDeck(deck.deck_id)">Delete</button>
    </div>
  </div>
</div>
</template>