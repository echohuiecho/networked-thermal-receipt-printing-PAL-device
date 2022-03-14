<template>
  <div
    class="full-height-wrapper full-width-wrapper
    d-flex flex-column justify-content-center align-items-center"
  >
    <transition name="fade">
      <div v-if="waitString" class="text-center">
        <h2 class="hk">
          後人類紀植物學習圖鑑整理中，請稍等...
        </h2>
        <h2 class="en">
          Preparing Post Anthropocene Learning Encyclopedia, please wait...
          <span class="typing-text"></span>
        </h2>
        <h1 class="en mt-5">
          {{ minutes }} : {{ seconds }}
        </h1>
      </div>
    </transition>
    <transition name="fade">
      <h2 v-if="displayPrintMsg" class="typing-text en">
        {{ displayString }}
      </h2>
    </transition>
    <transition name="fade">
      <router-link
        to="/"
        v-if="printStatus"
        class="position-absolute bottom-0 mb-5 text-muted text-decoration-none"
      >
        <div class="d-flex justify-content-center">
          <i class="material-icons">chevron_left</i>
          <h2 class="hk text-uppercase">返回</h2>
          <h2 class="en ms-2 text-uppercase mt-offset-2">Back</h2>
          <i class="material-icons">chevron_right</i>
        </div>
      </router-link>
    </transition>
  </div>
</template>

<script>
export default {
  props: ['plant'],
  data() {
    return {
      strings: [],
      displayPrintMsg: true,
      counter: 0,
      iterationCounter: 0,
      displayCounter: 0,
      displayString: '',
      displayForward: true,
      timeout: 120,
      waitString: false,
      printStatus: false,
      minutes: 7,
      seconds: 59,
      targetTime: 0,
      currentTime: 0,
      secondsLeft: 0,
      isInactive: false,
      userActivityThrottlerTimeout: null,
      userActivityTimeout: null,
    };
  },
  watch: {
    counter() {
      this.timeout = this.counter === 0 ? 120 : 50;
    },
    waitString() {
      if (this.waitString) {
        this.countdownWait();
      }
    },
  },
  methods: {
    displayText() {
      const textLength = this.strings[this.counter].length;
      if (this.displayPrintMsg) {
        setTimeout(() => {
          this.displayString = this.strings[this.counter].substring(0, this.displayCounter);
          if (this.displayForward) {
            this.displayCounter += 1;
            if (this.displayCounter <= textLength) {
              this.displayText();
            } else {
              this.displayForward = false;
              this.displayText();
            }
          } else {
            this.displayCounter -= 1;
            if (this.displayCounter >= 0) {
              this.displayText();
            } else {
              this.displayForward = true;
              this.counter = this.counter === 0 ? 1 : 0;
              this.displayText();
            }
          }
        }, this.timeout);
      }
    },
    format(n) {
      return (n < 10 ? '0' : '') + n;
    },
    getCountdown() {
      this.currentTime = new Date().getTime();
      this.secondsLeft = (this.targetTime - this.currentTime) / 1000;
      setTimeout(() => {
        this.minutes = this.format(parseInt(this.secondsLeft / 60, 10));
        this.seconds = this.format(parseInt(this.secondsLeft % 60, 10));
        if (this.secondsLeft > 1) {
          this.getCountdown();
        } else {
          this.printStatus = true;
          this.activateActivityTracker();
          this.resetUserActivityTimeout();
        }
      }, 1000);
    },
    initTimeNow() {
      this.targetTime = new Date().getTime() + 7 * 60 * 1000; // set the countdown date
      this.getCountdown();
    },
    countdownWait() {
      this.initTimeNow();
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
      }, 300000);
    },
    userActivityThrottler() {
      if (!this.userActivityThrottlerTimeout) {
        this.userActivityThrottlerTimeout = setTimeout(() => {
          this.resetUserActivityTimeout();

          clearTimeout(this.userActivityThrottlerTimeout);
          this.userActivityThrottlerTimeout = null;
        }, 300000);
      }
    },
    inactiveUserAction() {
      // logout logic
      console.log('inactive user');
      this.$router.push('/');
    },
  },
  mounted() {
    console.clear();
    this.strings.push(`${this.plant.hk} - 後人類紀植物學習圖鑑列印中...`);
    this.strings.push(
      `${this.plant.en} - Post Anthropocene Learning Encyclopedia printing in progress...`,
    );
    this.displayText();
    setTimeout(() => {
      // display loading info text
      this.waitString = true;
      this.displayPrintMsg = false;
    }, 195000);
    // setTimeout(() => {
    //   // print completed, set idle mode listener
    //   console.log('print completed');
    //   this.printStatus = true;
    //   this.activateActivityTracker();
    //   this.resetUserActivityTimeout();
    // }, 600000);
  },
  unmounted() {
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
