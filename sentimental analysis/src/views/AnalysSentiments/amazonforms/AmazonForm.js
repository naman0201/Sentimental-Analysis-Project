/* eslint-disable prettier/prettier */
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
} from '@coreui/react'
import { DocsCallout, DocsExample } from 'src/components'
import AmazonTable from './AmazonTable'
import AmazonAnaysis from './AmazonAnalysis'
const axios = require('axios').default

const weatherapi =
  'https://api.openweathermap.org/data/2.5/weather?appid=ca899a14f705fa4d8cbbefeacddfab55&units=metric&q=Bhopal'

const Tooltips = (setValidated, validated) => {
  const [shwMessage, setShwMessage] = useState(false)
  const handleSubmit = async (event) => {
    const form = event.currentTarget
    setShwMessage(true)

    if (form.checkValidity() === false) {
      event.preventDefault()
      event.stopPropagation()
    } else {
      // setValidated(true)
    }
    // event.preventDefault()
  }
  return (
    <CForm
      className="row g-3 needs-validation"
      noValidate
      validated={shwMessage}
      onSubmit={handleSubmit}
      action={'http://127.0.0.1:8000/dataview'}
    >
      <CCol md={8} className="position-relative">
        <CFormLabel htmlFor="validationTooltip01">Select Ecommerce Site to run analyse</CFormLabel>
        <CFormSelect id="validationTooltip01" defaultValue="" required>
          <option hidden>Select Ecommerce site</option>
          <option>Amazon</option>
          <option>Flipkart</option>
          <option>Meshow</option>
          <option>Myntra</option>
          <option>Shopee</option>
          <option>Snapdeal</option>
          <option>Too Good</option>
          <option>Zivame</option>
        </CFormSelect>
        <CFormFeedback tooltip invalid>
          Please provide a valid Ecommerce site.
        </CFormFeedback>
        <CFormFeedback tooltip valid>
          Looks Good!
        </CFormFeedback>
      </CCol>
      <CCol md={8} className="position-relative">
        <CFormLabel htmlFor="validationTooltip02">Enter the product Name</CFormLabel>
        <CFormInput
          type="text"
          id="validationTooltip02"
          required
          placeholder="eg: Smart Watch, Phone, Television"
        />
        <CFormFeedback tooltip valid>
          Looks good!
        </CFormFeedback>
        <CFormFeedback tooltip invalid>
          Please fill product name
        </CFormFeedback>
      </CCol>
      <CCol md={8} className="position-relative">
        <CFormLabel htmlFor="validationTooltip03">Enter the link of product</CFormLabel>
        <CFormInput
          type="url"
          id="validationTooltip03"
          required
          placeholder="eg: https://www.amazon.com/"
        />
        <CFormFeedback tooltip valid>
          Looks good!
        </CFormFeedback>
        <CFormFeedback tooltip invalid>
          Enter correct link
        </CFormFeedback>
      </CCol>
      <CCol xs={12} className="position-relative">
        <CButton color="info" type="submit">
          Check
        </CButton>
      </CCol>
    </CForm>
  )
}
const Validation = () => {
  // const [showTable, setTable] = useState(false)
  const [validated, setValidated] = useState(false)
  const [renderPage, setRenderPage] = useState(false)
  // useEffect(() => {
  //   return
  // }, [validated])
  let renderedElement = (
    <CRow>
      <CCol xs={12}>
        <CCard className="mb-4">
          <CCardHeader>
            <strong>Ecommerce</strong> <small>Analysis</small>
          </CCardHeader>
          <CCardBody>
            <DocsExample href="forms/validation#tooltips">
              {Tooltips(setValidated, validated)}
            </DocsExample>
          </CCardBody>
        </CCard>
      </CCol>
      {validated ? <AmazonTable handleRenderPage={setRenderPage} /> : null}
    </CRow>
  )

  return renderPage ? <AmazonAnaysis /> : renderedElement
}
export default Validation
