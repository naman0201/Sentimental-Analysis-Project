/* eslint-disable prettier/prettier */
/* eslint-disable react/prop-types */
import React, { useState, useEffect } from 'react'
import {
  CButton,
  CCard,
  CCardBody,
  CCardHeader,
  CCol,
  CForm,
  CFormCheck,
  CFormInput,
  CFormFeedback,
  CFormLabel,
  CFormSelect,
  CFormTextarea,
  CInputGroup,
  CInputGroupText,
  CRow,
  CSpinner,
} from '@coreui/react'
const axios = require('axios').default
const weatherapi =
  'https://api.openweathermap.org/data/2.5/weather?appid=ca899a14f705fa4d8cbbefeacddfab55&units=metric&q=Bhopal'
const AmazonAnaysis = (props) => {
  const [apiData, setApiData] = useState({})
  useEffect(() => {
    async function fetchMyAPI() {
      await axios
        .get(weatherapi)
        .then((response) => {
          console.log(response)
          setApiData(response)
        })
        .catch((err) => {
          console.log(err)
        })
    }
    fetchMyAPI()
  }, [])
  console.log(apiData)
  return (
    <CRow>
      <CCol xs={12}>
        <CCard className="mb-4">
          <CCardHeader>
            <strong>Ecommerce</strong> <small>Analysis Table</small>
          </CCardHeader>
          <CCardBody>
            <p>{apiData.data ? JSON.stringify(apiData.data.coord) : <CSpinner color="danger" />}</p>
          </CCardBody>
        </CCard>
      </CCol>
    </CRow>
  )
}
export default AmazonAnaysis
