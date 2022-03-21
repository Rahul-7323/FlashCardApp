import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '@/views/Dashboard.vue';
import Page from '@/views/Page.vue';
import Login from '@/views/Login.vue'
import Register from '@/views/Register.vue'
import Home from '@/views/Home.vue'
import Decks from '@/views/Decks.vue'
import AddDeck from '@/views/AddDeck.vue';
import AddCard from '@/views/AddCard.vue';
import { useAuthStore } from '@/stores/AuthStore';
import UserInfo from '@/views/UserInfo.vue';
import DeckCards from '@/views/DeckCards.vue';


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
            { path: 'decks', name: 'Decks', component: Decks },
            { path: 'decks/:id', name: 'Deck Cards', component: DeckCards },
            { path: 'userinfo', name: 'UserInfo', component: UserInfo },
            { path: 'add-deck', name: 'Add Deck', component: AddDeck },
            { path: 'add-card', name: 'Add Card', component: AddCard },
        ]
    },
    { path: '/login', name: 'Login', component: Login },
    { path: '/register', name: 'Register', component: Register },
    { path: '/:pathMatch(.*)*', redirect: '/home' },
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

router.beforeEach( (to, from) => {
    const AuthStore = useAuthStore();
    if (to.meta.requiresAuth && !AuthStore.isAuthenticated) {
        return {
            path: '/login',
        }
    }
    else if((to.name == 'Login' || to.name == 'Register') && AuthStore.isAuthenticated){
        console.log("Already Authenticated");
        return {
            path: '/dashboard'
        }
    }
    return true;
})

export default router;