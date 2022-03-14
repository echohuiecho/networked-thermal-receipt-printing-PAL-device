<template lang="">
  <transition name="fade">
    <Overlay
    v-if="!overlayDone"
    @close-overlay="closeOverlay"
    >
    </Overlay>
  </transition>
  <transition name="fade">
    <PrintWidget
      v-if="printWidget"
      :plant="selectedPlant"
      @close-print-widget="closePrintWidget"
    >
    </PrintWidget>
  </transition>
  <div class="row g-0">
    <a
      v-for="plant in plants"
      :key="plant.nameEn"
      @click.prevent="printPlant(plant)"
      class="text-decoration-none col-3 grid-img-wrapper position-relative"
    >
      <img :src="`${(publicPath, plant.src)}`" alt=""
      class="w-100 h-100 img-object-fit"
      @load="onImgLoad" />
      <div class="position-absolute bottom-0 ms-3 mb-3">
        <div class="hk text-dark">{{ plant.nameHk }}</div>
        <div class="en text-dark">{{ plant.nameEn }}</div>
      </div>
    </a>
  </div>
  <transition name="fade">
    <div v-if="scrollWidget"
      class="position-fixed bottom-0 text-info text-center w-100 mb-5">
      <ScrollDownWidget></ScrollDownWidget>
    </div>
  </transition>
</template>

<script>
import Overlay from '@/components/Overlay.vue';
import PrintWidget from '@/components/PrintWidget.vue';
import ScrollDownWidget from '@/components/ScrollDownWidget.vue';

export default {
  data() {
    return {
      publicPath: process.env.BASE_URL,
      scrollWidget: true,
      plants: [
        {
          nameHk: '香蕉',
          nameEn: 'Banana',
          src: 'plants/banana.jpg',
          link: '/print/banana',
        },
        {
          nameHk: '燈籠椒',
          nameEn: 'Bell Pepper',
          src: 'plants/bellpepper.jpg',
          link: '/print/bell-pepper',
        },
        {
          nameHk: '苦瓜',
          nameEn: 'Bitter Melon',
          src: 'plants/bittermelon.jpg',
          link: '/print/bitter-melon',
        },
        {
          nameHk: '韭菜',
          nameEn: 'Chinese Chive',
          src: 'plants/chinesechive.jpg',
          link: '/print/chinese-chive',
        },
        {
          nameHk: '芥蘭',
          nameEn: 'Chinese Kale',
          src: 'plants/chinesekale.jpg',
          link: '/print/chinese-kale',
        },
        {
          nameHk: '菜心',
          nameEn: 'Choysum',
          src: 'plants/choysum.jpg',
          link: '/print/choy-sum',
        },
        {
          nameHk: '粟米',
          nameEn: 'Corn',
          src: 'plants/corn.jpg',
          link: '/print/corn',
        },
        {
          nameHk: '青瓜',
          nameEn: 'Cucumber',
          src: 'plants/cucumber.jpg',
          link: '/print/cucumber',
        },
        {
          nameHk: '茄子',
          nameEn: 'Eggplant',
          src: 'plants/eggplant.jpg',
          link: '/print/egg-plant',
        },
        {
          nameHk: '秋葵',
          nameEn: 'Okra',
          src: 'plants/okra.jpg',
          link: '/print/okra',
        },
        {
          nameHk: '木瓜',
          nameEn: 'Papaya',
          src: 'plants/papaya.jpg',
          link: '/print/papaya',
        },
        {
          nameHk: '薯仔',
          nameEn: 'Potato',
          src: 'plants/potato.jpg',
          link: '/print/potato',
        },
        {
          nameHk: '稻米',
          nameEn: 'Rice',
          src: 'plants/rice.jpg',
          link: '/print/rice',
        },
        {
          nameHk: '麥',
          nameEn: 'Rye',
          src: 'plants/rye.jpg',
          link: '/print/rye',
        },
        {
          nameHk: '荷蘭豆',
          nameEn: 'Snow Pea',
          src: 'plants/snowpea.jpg',
          link: '/print/snow-pea',
        },
        {
          nameHk: '菠菜',
          nameEn: 'Spinach',
          src: 'plants/spinach.jpg',
          link: '/print/spinach',
        },
        {
          nameHk: '蕃薯',
          nameEn: 'Sweet Potato',
          src: 'plants/sweetpotato.jpg',
          link: '/print/sweet-potato',
        },
        {
          nameHk: '芋頭',
          nameEn: 'Taro',
          src: 'plants/taro.jpg',
          link: '/print/taro',
        },
        {
          nameHk: '蕃茄',
          nameEn: 'Tomato',
          src: 'plants/tomato.jpg',
          link: '/print/tomato',
        },
        {
          nameHk: '通菜',
          nameEn: 'Water Spinach',
          src: 'plants/waterspinach.jpg',
          link: '/print/water-spinach',
        },
      ],
      printWidget: false,
      selectedPlant: {},
      imgLoadLog: 0,
      imgLoaded: false,
      overlayDone: false,
      isInactive: false,
      userActivityThrottlerTimeout: null,
      userActivityTimeout: null,
    };
  },
  components: {
    Overlay,
    ScrollDownWidget,
    PrintWidget,
  },
  watch: {
    // hide overflow class when images are loaded
    // imgLoaded() {
    //   if (this.imgLoaded) {
    //     const body = document.getElementsByTagName('body')[0];
    //     body.classList.remove('overflow-hidden');
    //   }
    // },
    // hide overflow class when overlay is hidden
    overlayDone() {
      if (this.overlayDone) {
        const body = document.getElementsByTagName('body')[0];
        body.classList.remove('overflow-hidden');
      }
    },
  },
  methods: {
    onImgLoad() {
      this.imgLoadLog += 1;
      // if (this.overlayDone && this.imgLoadLog === 20) {
      //   this.imgLoaded = true;
      // }
      if (this.imgLoadLog === 20) {
        this.imgLoaded = true;
      }
    },
    closeOverlay() {
      this.overlayDone = true;
      // All images loaded into page, close overlay
      // if (this.imgLoadLog === 20) {
      //   setTimeout(() => {
      //     this.imgLoaded = true;
      //   }, 500);
      // }
    },
    printPlant(plant) {
      this.printWidget = true;
      this.selectedPlant = plant;
    },
    closePrintWidget() {
      this.printWidget = false;
    },
    activateActivityTracker() {
      window.addEventListener('mousemove', this.resetUserActivityTimeout);
      window.addEventListener('scroll', this.resetUserActivityTimeout);
      window.addEventListener('keydown', this.resetUserActivityTimeout);
      window.addEventListener('resize', this.resetUserActivityTimeout);
    },
    resetUserActivityTimeout() {
      clearTimeout(this.userActivityTimeout);
      this.userActivityTimeout = setTimeout(() => {
        this.inactiveUserAction();
      }, 60000);
    },
    userActivityThrottler() {
      if (!this.userActivityThrottlerTimeout) {
        this.userActivityThrottlerTimeout = setTimeout(() => {
          this.resetUserActivityTimeout();

          clearTimeout(this.userActivityThrottlerTimeout);
          this.userActivityThrottlerTimeout = null;
        }, 60000);
      }
    },
    inactiveUserAction() {
      // logout logic
      console.log('inactive user');
      if (this.overlayDone) {
        this.overlayDone = false;
      }
    },
    scrollHandler() {
      const windowY = window.scrollY;
      if (windowY >= 350) {
        this.scrollWidget = false;
      } else {
        this.scrollWidget = true;
      }
    },
  },
  mounted() {
    document.addEventListener('scroll', this.scrollHandler);
    this.activateActivityTracker();
  },
  unmounted() {
    document.removeEventListener('scroll', this.scrollHandler);

    window.removeEventListener('mousemove', this.userActivityThrottler);
    window.removeEventListener('scroll', this.userActivityThrottler);
    window.removeEventListener('keydown', this.userActivityThrottler);
    window.removeEventListener('resize', this.userActivityThrottler);
    window.removeEventListener('mousemove', this.resetUserActivityTimeout);
    window.removeEventListener('scroll', this.resetUserActivityTimeout);
    window.removeEventListener('keydown', this.resetUserActivityTimeout);
    window.removeEventListener('resize', this.resetUserActivityTimeout);

    clearTimeout(this.userActivityTimeout);
    clearTimeout(this.userActivityThrottlerTimeout);
    clearTimeout(this.resetUserActivityTimeout);
  },
};
</script>
