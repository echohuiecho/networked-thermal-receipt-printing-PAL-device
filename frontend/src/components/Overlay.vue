<template>
  <div
    class="position-fixed full-height-wrapper full-width-wrapper
    d-flex flex-column justify-content-center align-items-center bg-body zIndexModal"
  >
    <h2 class="typing-text en">{{ displayString }}</h2>
    <transition name="fade">
      <a
        v-if="enterStatus"
        class="position-absolute bottom-0 mb-5 text-secondary text-decoration-none"
        @click="$emit('close-overlay')"
      >
        <div class="d-flex align-items-center">
          <i class="material-icons">chevron_left</i>
          <h2 class="en text-uppercase">Enter</h2>
          <i class="material-icons">chevron_right</i>
        </div>
      </a>
    </transition>
  </div>
</template>

<script>
export default {
  props: ['plant'],
  data() {
    return {
      strings: [
        '後人類紀植物學習圖鑑',
        'Post Anthropocene Learning Encyclopedia',
      ],
      counter: 0,
      iterationCounter: 0,
      displayCounter: 0,
      displayString: '',
      displayForward: true,
      timeout: 80,
      enterStatus: false,
      printStatus: false,
    };
  },
  watch: {
    counter() {
      this.timeout = this.counter === 0 ? 110 : 70;
    },
  },
  methods: {
    displayText() {
      const textLength = this.strings[this.counter].length;
      // display only one loop
      // if (this.iterationCounter <= 2) {
      //   setTimeout(() => {
      //     this.displayString = this.strings[this.counter].substring(0, this.displayCounter);
      //     if (this.displayForward) {
      //       this.displayCounter += 1;
      //       if (this.displayCounter <= textLength) {
      //         this.displayText();
      //       } else {
      //         this.iterationCounter += 1;
      //         this.displayForward = false;
      //         this.displayText();
      //       }
      //     } else {
      //       this.displayCounter -= 1;
      //       if (this.displayCounter >= 0) {
      //         this.displayText();
      //       } else {
      //         this.iterationCounter += 1;
      //         this.displayForward = true;
      //         this.counter = this.counter === 0 ? 1 : 0;
      //         this.displayText();
      //       }
      //     }
      //   }, this.timeout);
      // } else {
      //   this.$emit('close-overlay');
      // }
      setTimeout(() => {
        this.displayString = this.strings[this.counter].substring(0, this.displayCounter);
        if (this.displayForward) {
          this.displayCounter += 1;
          if (this.displayCounter <= textLength) {
            this.displayText();
          } else {
            this.iterationCounter += 1;
            this.displayForward = false;
            this.displayText();
          }
        } else {
          this.displayCounter -= 1;
          if (this.displayCounter >= 0) {
            this.displayText();
          } else {
            this.iterationCounter += 1;
            this.displayForward = true;
            this.counter = this.counter === 0 ? 1 : 0;
            this.displayText();
          }
        }
      }, this.timeout);
    },
  },
  mounted() {
    console.clear();
    const body = document.getElementsByTagName('body')[0];
    body.classList.add('overflow-hidden');
    setTimeout(() => {
      this.enterStatus = true;
    }, 5000);
    this.displayText();
  },
};
</script>
