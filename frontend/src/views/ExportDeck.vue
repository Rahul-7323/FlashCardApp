<script>
import { useAuthStore } from '@/stores/AuthStore';

export default {
    setup(){
        const AuthStore = useAuthStore();
        return { AuthStore }
    },
    data() {
        return {
            messages: []
        }
    },
    mounted() {
        const source = this.AuthStore.eventSource;
        source.addEventListener('SSE_TEST', (e) => {
            const data = JSON.parse(e.data);
            this.messages.push(data.message);
        },false);
    }
}
</script>

<template>
<div class="text-xl">Messages from Flask-SSE</div>
<ul>
    <li v-for="message in messages">{{ message }}</li>
</ul>
</template>