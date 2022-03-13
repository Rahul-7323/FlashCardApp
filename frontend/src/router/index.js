import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '@/views/Dashboard.vue';
import Review from '@/views/Review.vue';
import Page from '@/views/Page.vue';
import Login from '@/views/Login.vue'
import Register from '@/views/Register.vue'
import Home from '@/views/Home.vue'
import Decks from '@/views/Decks.vue'

const routes = [
    { path: '/home', name: 'Home', component: Home },
    { path: '/', redirect: '/home' },
    {
        path: '/',
        name: 'Page',
        component: Page,
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

export default router;