/* eslint-disable prettier/prettier */
import React, { useState } from 'react'
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
const Tooltips = () => {
  const [validated, setValidated] = useState(false)
  const handleSubmit = (event) => {
    const form = event.currentTarget
    if (form.checkValidity() === false) {
      event.preventDefault()
      event.stopPropagation()
    }
    setValidated(true)
  }
  return (
    <CForm
      className="row g-3 needs-validation"
      noValidate
      validated={validated}
      onSubmit={handleSubmit}
    >
      <CCol md={8} className="position-relative">
        <CFormLabel htmlFor="validationTooltip01">Name or place</CFormLabel>
        <CFormInput
          type="text"
          id="validationTooltip01"
          required
          placeholder="Name of person or place"
        />
        <CFormFeedback tooltip valid>
          Looks good!
        </CFormFeedback>
        <CFormFeedback tooltip invalid>
          Please fill this field
        </CFormFeedback>
      </CCol>

      <CCol md={8} className="position-relative">
        <CFormLabel htmlFor="validationTooltip02">Category:</CFormLabel>
        <CFormSelect id="validationTooltip02" required>
          <option selected hidden value="">
            Select category
          </option>
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
          Please provide a valid category.
        </CFormFeedback>
        <CFormFeedback tooltip valid>
          Looks Good!
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
  return (
    <CRow>
      <CCol xs={12}>
        <CCard className="mb-4">
          <CCardHeader>
            <strong>Twitter</strong> <small>Tweets</small>
          </CCardHeader>
          <CCardBody>
            <DocsExample href="forms/validation#tooltips">{Tooltips()}</DocsExample>
          </CCardBody>
        </CCard>
      </CCol>
    </CRow>
  )
}
export default Validation
