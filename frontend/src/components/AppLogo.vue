<script>
import { RouterLink } from "vue-router";

export default {
    components: {
        RouterLink,
    }
}
</script>

<template>
    <RouterLink to="/">
        <img
            src="/FlashCardApp-logo.png"
            alt="FlashCardApp-logo"
            class="w-full h-20 object-cover rounded-lg shadow-xl bg-black"
        />
    </RouterLink>
</template>