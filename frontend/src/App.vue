<script setup>
import { RouterView } from 'vue-router';
import { useAppStore } from '@/stores/AppStore';
import { useAuthStore } from '@/stores/AuthStore';
import { onBeforeUnmount } from 'vue';

const AppStore = useAppStore();
AppStore.getTheme();

const AuthStore = useAuthStore();
AuthStore.authFromSessionStorage();

onBeforeUnmount(() => {
  AuthStore.logout();
})

</script>

<template>
  <RouterView />
</template>