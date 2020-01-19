<template>
  <div>
    <h1>new form</h1>

    <v-form v-on:submit.prevent="submit">
      <v-container fluid>
        <v-row align="center">
          <v-col class="d-flex" cols="12" sm="6">
            <v-text-field v-model="srtid" label="srtid"></v-text-field>
          </v-col>

          <v-col class="d-flex" cols="12" sm="6">
            <v-text-field v-model="srtpw" label="srtpw"></v-text-field>
          </v-col>

          <v-col class="d-flex" cols="12" sm="6">
            <v-text-field v-model="logintype" label="logintype"></v-text-field>
          </v-col>

          <v-col class="d-flex" cols="12" sm="6">
            <v-text-field v-model="phone" label="phone"></v-text-field>
          </v-col>

          <v-col class="d-flex" cols="12" sm="6">
            <v-text-field v-model="dpt" label="dpt"></v-text-field>
          </v-col>

          <v-col class="d-flex" cols="12" sm="6">
            <v-text-field v-model="arr" label="arr"></v-text-field>
          </v-col>

          <v-col class="d-flex" cols="12" sm="6">
            <v-text-field v-model="adult" label="adult"></v-text-field>
          </v-col>

          <v-col class="d-flex" cols="12" sm="6">
            <v-text-field v-model="child" label="child"></v-text-field>
          </v-col>

          <v-col class="d-flex" cols="12" sm="6">
            <v-text-field v-model="date" label="date"></v-text-field>
          </v-col>

          <v-col class="d-flex" cols="12" sm="6">
            <v-text-field v-model="dptime" label="dptime"></v-text-field>
          </v-col>

          <v-col class="d-flex" cols="12" sm="6">
            <v-text-field v-model="ticketnum" label="ticketnum"></v-text-field>
          </v-col>
        </v-row>
      </v-container>

      <button>등록하기</button>
    </v-form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      srtid: "01021843577",
      srtpw: "Sphv84031!@",
      logintype: "3",
      dpt: "동탄",
      arr: "수서",
      adult: "1",
      child: "0",
      date: "2020-01-18",
      dptime: "14",
      ticketnum: "4",
      phone: "me"
    };
  },
  methods: {
    submit() {
      this.$store.dispatch("post/register_ticket", {
        srtid: this.srtid,
        srtpw: this.srtpw,
        logintype: this.logintype,
        phone: this.phone,
        dpt: this.dpt,
        arr: this.arr,
        adult: this.adult,
        child: this.child,
        date: this.date,
        dptime: this.dptime,
        ticketnum: this.ticketnum
      });
    }
  }
};
</script>
