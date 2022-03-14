import { createRouter, createWebHashHistory } from 'vue-router';

const routes = [
  {
    path: '/',
    name: 'Front Layout',
    component: () => import('@/views/front/Index.vue'),
    children: [
      {
        path: '',
        name: 'Home',
        component: () => import('@/views/front/Home.vue'),
      },
      {
        path: 'ping',
        name: 'Ping',
        component: () => import('@/views/front/Ping.vue'),
      },
      {
        path: 'print/banana',
        name: 'PrintBanana',
        component: () => import('@/views/front/print/Banana.vue'),
      },
      {
        path: 'print/bell-pepper',
        name: 'PrintBellPepper',
        component: () => import('@/views/front/print/BellPepper.vue'),
      },
      {
        path: 'print/bitter-melon',
        name: 'PrintBitterMelon',
        component: () => import('@/views/front/print/BitterMelon.vue'),
      },
      {
        path: 'print/chinese-chive',
        name: 'PrintChineseChive',
        component: () => import('@/views/front/print/ChineseChive.vue'),
      },
      {
        path: 'print/chinese-kale',
        name: 'PrintChineseKale',
        component: () => import('@/views/front/print/ChineseKale.vue'),
      },
      {
        path: 'print/choy-sum',
        name: 'PrintChoysum',
        component: () => import('@/views/front/print/ChoySum.vue'),
      },
      {
        path: 'print/corn',
        name: 'PrintCorn',
        component: () => import('@/views/front/print/Corn.vue'),
      },
      {
        path: 'print/cucumber',
        name: 'PrintCucumber',
        component: () => import('@/views/front/print/Cucumber.vue'),
      },
      {
        path: 'print/egg-plant',
        name: 'PrintEggplant',
        component: () => import('@/views/front/print/Eggplant.vue'),
      },
      {
        path: 'print/okra',
        name: 'PrintOkra',
        component: () => import('@/views/front/print/Okra.vue'),
      },
      {
        path: 'print/papaya',
        name: 'PrintPapaya',
        component: () => import('@/views/front/print/Papaya.vue'),
      },
      {
        path: 'print/potato',
        name: 'PrintPotato',
        component: () => import('@/views/front/print/Potato.vue'),
      },
      {
        path: 'print/rice',
        name: 'PrintRice',
        component: () => import('@/views/front/print/Rice.vue'),
      },
      {
        path: 'print/rye',
        name: 'PrintRye',
        component: () => import('@/views/front/print/Rye.vue'),
      },
      {
        path: 'print/snow-pea',
        name: 'PrintSnowPea',
        component: () => import('@/views/front/print/SnowPea.vue'),
      },
      {
        path: 'print/spinach',
        name: 'PrintSpinach',
        component: () => import('@/views/front/print/Spinach.vue'),
      },
      {
        path: 'print/sweet-potato',
        name: 'PrintSweetPotato',
        component: () => import('@/views/front/print/SweetPotato.vue'),
      },
      {
        path: 'print/taro',
        name: 'PrintTaro',
        component: () => import('@/views/front/print/Taro.vue'),
      },
      {
        path: 'print/tomato',
        name: 'PrintTomato',
        component: () => import('@/views/front/print/Tomato.vue'),
      },
      {
        path: 'print/water-spinach',
        name: 'PrintWaterSpinach',
        component: () => import('@/views/front/print/WaterSpinach.vue'),
      },
    ],
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
  scrollBehavior() {
    // always scroll to top
    return { top: 0 };
  },
});

export default router;
