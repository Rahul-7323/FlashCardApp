<script setup>
import { RouterView } from 'vue-router';
import { useAppStore } from '@/stores/AppStore';

const AppStore = useAppStore()
AppStore.getTheme()
</script>

<template>
  <RouterView />
</template>