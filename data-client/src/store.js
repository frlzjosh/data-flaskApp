import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    incidentNumber: null,
    offenseCode: null,
    offenseCodeGroup: null,
    offenseDescription: null,
    district: null,
    district: null,
    reportingArea: null,
    shooting: null,
    occuredOnDate: null,
    year: null,
    month: null,
    dayOfWeek: null,
    hour: null,
    ucrPart: null,
    street: null,
  },
  getters: {
    getIncidentNumber: state => {
      return state.incidentNumber
    }
  },
  mutations: {
    GET_INCIDENT_NUMBER(state, payload){
      state.incidentNumber = payload;
    }

  },
  actions: {
    storeDataIntoState({commit}, payload){
      console.log(payload.INCIDENT_NUMBER);
      commit('GET_INCIDENT_NUMBER', payload.INCIDENT_NUMBER)
    }
  }
})
