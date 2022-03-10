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
    <RouterLink
        :to="link"
        class="btn shadow-lg btn-info shadow-blue-400 dark:btn-warning dark:shadow-orange-300"
    >{{ name }}</RouterLink>
</template>