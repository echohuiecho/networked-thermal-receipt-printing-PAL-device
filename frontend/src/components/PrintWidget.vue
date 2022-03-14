<template>
  <div
    class="position-fixed full-height-wrapper full-width-wrapper
    d-flex flex-column justify-content-center align-items-center bg-body zIndexModal"
  >
    <div class="wrapper text-center">
      <h2 class="hk">列印 - {{ plant.nameHk }}</h2>
      <h2 class="en">Print - {{ plant.nameEn }}</h2>
      <div class="row-wrapper d-flex justify-content-between mt-5">
        <a href=""
          class="d-flex flex-column align-items-center text-decoration-none text-secondary"
          @click.prevent="closeModal"
        >
          <span class="hk">取消</span>
          <span class="en">Cancel</span>
        </a>
        <div class="solid-break"></div>
        <router-link
          :to="plant.link"
          class="d-flex flex-column align-items-center text-decoration-none text-white"
        >
          <span class="hk">確定</span>
          <span class="en">Yes</span>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['plant'],
  data() {
    return {
    };
  },
  methods: {
    closeModal() {
      this.$emit('closePrintWidget');
      const body = document.getElementsByTagName('body')[0];
      body.classList.remove('overflow-hidden');
    },
  },
  mounted() {
    console.clear();
    const body = document.getElementsByTagName('body')[0];
    body.classList.add('overflow-hidden');
  },
};
</script>
