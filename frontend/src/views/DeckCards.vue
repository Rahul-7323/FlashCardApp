<script>
import { useUserStore } from "@/stores/UserStore";
import CardsItem from '@/components/CardsItem.vue';

export default {
    setup() {
        const UserStore = useUserStore();
        return { UserStore };
    },
    computed: {
        cards() {
            console.log(this.$route.params.id);
            return this.UserStore.getCardsByDeckId(this.$route.params.id);
        }
    },
    components: { CardsItem }
}
</script>

<template>
<div>
    <div v-if="cards.length === 0" class="flex flex-row align-middle justify-center">
        <div class="text-3xl">There are no cards!</div>
    </div>
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
        <CardsItem v-for="card in cards" :card="card" />
    </div>
</div>
</template>