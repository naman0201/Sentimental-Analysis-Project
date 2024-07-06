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
      <CCol md={5} className="position-relative">
        <CFormLabel htmlFor="validationTooltip01">Name</CFormLabel>
        <CFormInput type="text" id="validationTooltip01" placeholder="Name of person" required />
        <CFormFeedback tooltip valid>
          Looks good!
        </CFormFeedback>
        <CFormFeedback tooltip invalid>
          Please type a name.
        </CFormFeedback>
      </CCol>
      <CCol md={5} className="position-relative">
        <CFormLabel htmlFor="validationTooltip02">Age</CFormLabel>
        <CFormInput type="number" id="validationTooltip02" placeholder="Age of person" required />
        <CFormFeedback tooltip valid>
          Looks good!
        </CFormFeedback>
        <CFormFeedback tooltip invalid>
          Please input correct age
        </CFormFeedback>
      </CCol>
      <CCol md={10} className="position-relative">
        <CFormLabel htmlFor="validationTooltip03">Address Line 1</CFormLabel>
        <CFormInput
          type="text"
          id="validationTooltip03"
          placeholder="Street address, P.O. box, company name, c/o"
          required
        />
        <CFormFeedback tooltip valid>
          Looks good!
        </CFormFeedback>
        <CFormFeedback tooltip invalid>
          Please type address here.
        </CFormFeedback>
      </CCol>

      <CCol md={10} className="position-relative">
        <CFormLabel htmlFor="validationTooltip04">Address Line 2</CFormLabel>
        <CFormInput
          type="text"
          id="validationTooltip04"
          placeholder="Apartment, suite, unit, building, floor, etc"
          required
        />
        <CFormFeedback tooltip valid>
          Looks good!
        </CFormFeedback>
        <CFormFeedback tooltip invalid>
          Please type address here.
        </CFormFeedback>
      </CCol>
      <CCol md={5} className="position-relative">
        <CFormLabel htmlFor="validationTooltip05">Case Study File</CFormLabel>
        <CFormInput type="file" id="validationTooltip05" aria-label="file example" required />
        <CFormFeedback tooltip invalid>
          Invalid file
        </CFormFeedback>
      </CCol>
      <CCol md={5} className="position-relative">
        <CFormLabel htmlFor="validationTooltip06">Upload a photo</CFormLabel>
        <CFormInput type="file" id="validationTooltip06" aria-label="file example" required />
        <CFormFeedback tooltip invalid>
          Please upload a photo
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
            <strong>Criminal</strong> <small>Activities Analysis</small>
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
