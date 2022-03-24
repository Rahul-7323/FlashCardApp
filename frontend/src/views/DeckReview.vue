<script>
import { useUserStore } from '@/stores/UserStore';
import ReviewCard from '@/components/ReviewCard.vue';

export default {
    components: {
        ReviewCard,
    },
    setup() {
        const UserStore = useUserStore();
        return { UserStore };
    },
    computed: {
        cards() {
            return (this.UserStore.getCardsByDeckId(this.$route.params.id)).sort( () => Math.random()-0.5 );
        },
    },
    data() {
        return {
            count: 0,
            result: [],
        }
    },
    methods: {
        nextCard(card_id,diff,score) {
            this.result.push({'card_id':card_id,'difficulty':diff,'score':score});
            if(this.count == (this.cards.length - 1)){
                this.UserStore.doReview(this.$route.params.id,this.result);
                this.$router.push('/decks');
            }
            this.count++;
        }
    },
}
</script>

<template>
<div v-if="cards.length === 0" class="flex flex-row align-middle justify-center">
    <div class="text-3xl">There are no cards!</div>
</div>
<ReviewCard v-else @next-card="(card_id,diff,score) => nextCard(card_id,diff,score)" :card="cards[count]" :key="cards[count]"/>
</template>