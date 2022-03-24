<script>
import { useUserStore } from '@/stores/UserStore';

export default {
    setup() {
      const UserStore = useUserStore();
      return { UserStore }
    },
    props: {
        card: {
            default: {}
        }
    }
}
</script>

<template>
<div class="card bg-base-100 cool-shadow">
  <div class="card-body p-5 flex flex-col">
    <div class="px-1 py-1 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
      <dt class="text-sm font-medium">Front</dt>
      <dd class="mt-1 text-sm sm:mt-0 sm:col-span-2 break-all">{{ card.front }}</dd>
    </div>
    <div class="px-1 py-1 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
      <dt class="text-sm font-medium">Back</dt>
      <dd class="mt-1 text-sm sm:mt-0 sm:col-span-2 break-all">{{ card.back }}</dd>
    </div>
    <div class="card-actions justify-start">
      <button class="btn btn-xs btn-error" @click="UserStore.deleteCard(card.card_id)">Delete</button>
    </div>
  </div>
</div>
</template>