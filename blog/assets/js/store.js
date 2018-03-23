/**
 * Created by develop on 9/01/18.
 */
import { createStore } from 'redux';
import moment from 'moment';

const initialState = {
    update: false,
    selects: {
        users: "",
        tipoFactura : "",
        tipoServicio : ""
    },
    datepickers :{
        fechaInicio : moment().subtract(4, 'months').format('DD/MM/YYYY'),
        fechaFinal : moment().format('DD/MM/YYYY')
    },
    dataTable:{
        results : []
    },
    modals : {

    }
};

function switchResult(state, action){
    return {
        ...state,
        update: true
    }
}

const reducer = function (state, action) {

    return switchResult(state, action);
};

const store = createStore(
    reducer,
    initialState,
    window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
);


export default store;
