<script>
import { useUserStore } from "@/stores/UserStore";
import DecksItem from "@/components/DecksItem.vue";

export default {
    setup() {
        const UserStore = useUserStore();
        return { UserStore };
    },
    computed: {
        decks() {
            return this.UserStore.decks;
        }
    },
    components: { DecksItem }
}
</script>

<template>
<div>
    <div v-if="decks.length === 0" class="flex flex-row align-middle justify-center">
        <div class="text-3xl">There are no decks!</div>
    </div>
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
        <DecksItem v-for="deck in decks" :deck="deck" />
    </div>
</div>
</template>