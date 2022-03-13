<script>
import { useUserStore } from "@/stores/UserStore";
import LoadingSpinner from "@/components/LoadingSpinner.vue";

export default {
    components: {
        LoadingSpinner,
    },
    setup() {
        const UserStore = useUserStore();
        return { UserStore }
    },
    data() {
        return {
            showLoadingIcon: true,
        }
    },
    computed: {
        decks() {
            return this.UserStore.decks;
        },
    },
    mounted() {
        const self = this;
        const handler = setInterval(() => {
            if (self.decks.length > 0) {
                self.showLoadingIcon = false;
            }
        })
        setTimeout(() => {
            clearInterval(handler);
            this.showLoadingIcon = false;
        }, 3000)
    }
}
</script>

<template>
    <div class="bg-base-100 p-5 rounded-xl cool-shadow">
        <div class="relative h-full">
            <div class="absolute w-full h-full overflow-auto">
                <table class="table table-compact w-full">
                    <!-- head -->
                    <thead>
                        <tr>
                            <th></th>
                            <th>Deck Name</th>
                            <th>Last Review Time</th>
                            <th>Total Score</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(deck, index) in decks" class="hover">
                            <th>{{ index + 1 }}</th>
                            <td>{{ deck.deck_name }}</td>
                            <td>{{ deck.last_review_time }}</td>
                            <td>{{ deck.total_score }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div
                v-if="showLoadingIcon"
                class="h-full w-full flex flex-col justify-center text-center text-2xl"
            >
                <LoadingSpinner class="m-auto" />
            </div>
            <div
                v-else-if="decks.length == 0"
                class="h-full w-full flex flex-col justify-center text-center text-2xl"
            >There are no decks!</div>
        </div>
    </div>
</template>