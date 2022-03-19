import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '@/views/Dashboard.vue';
import Review from '@/views/Review.vue';
import Page from '@/views/Page.vue';
import Login from '@/views/Login.vue'
import Register from '@/views/Register.vue'
import Home from '@/views/Home.vue'
import Decks from '@/views/Decks.vue'
import { useAuthStore } from '@/stores/AuthStore';


const routes = [
    { path: '/home', name: 'Home', component: Home },
    { path: '/', redirect: '/home' },
    {
        path: '/',
        name: 'Page',
        component: Page,
        meta: { requiresAuth: true },
        children: [
            { path: 'Dashboard', name: 'Dashboard', component: Dashboard },
            { path: 'review', name: 'Review', component: Review },
            { path: 'decks', name: 'Decks', component: Decks }
        ]
    },
    { path: '/login', name: 'Login', component: Login },
    { path: '/register', name: 'Register', component: Register },
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

router.beforeEach((to, from) => {
    const AuthStore = useAuthStore();
    if (to.meta.requiresAuth && !AuthStore.isAuthenticated) {
        return {
            path: '/login',
            // save the location we were at to come back later
            query: { redirect: to.fullPath },
        }
    }
    return true;
})

export default router;