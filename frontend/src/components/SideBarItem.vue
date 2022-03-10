<script>
import { RouterLink } from "vue-router"
export default {
    props: ['link', 'name'],
    components: {
        RouterLink,
    }
}
</script>

<template>
    <RouterLink :to="link" class="btn btn-warning shadow-2xl">{{ name }}</RouterLink>
</template>