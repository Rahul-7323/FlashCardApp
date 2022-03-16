<script>
import { RouterLink } from "vue-router"
export default {
    props: ['link', 'name'],
    components: {
        RouterLink,
    },
    methods: {
        closeSidebar() {
            if (window.innerWidth <= 1024) {
                const elem = document.getElementsByClassName('drawer-toggle');
                if (elem) {
                    elem[0].checked = !elem[0].checked;
                }
            }
        }
    }
}
</script>

<template>
    <RouterLink
        :to="link"
        @click="closeSidebar"
        class="btn shadow-lg btn-info shadow-blue-400 dark:btn-warning dark:shadow-orange-300"
    >{{ name }}</RouterLink>
</template>