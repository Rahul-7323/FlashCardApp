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
    <div class="flex flex-row flex-wrap justify-evenly gap-5">
        <DecksItem v-for="deck in decks" :deck="deck" />
        <DecksItem />
    </div>
</template>