import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '@/views/Dashboard.vue'
import Review from '@/views/Review.vue';

const routes = [
    { path: '/', name: 'Dashboard', component: Dashboard },
    { path: '/review', name: 'Review', component: Review }
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;