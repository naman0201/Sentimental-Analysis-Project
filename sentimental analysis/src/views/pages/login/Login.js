import React, { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import {
  CButton,
  CFormLabel,
  CFormFeedback,
  CCard,
  CCardBody,
  CCardGroup,
  CCol,
  CContainer,
  CForm,
  CFormInput,
  CInputGroup,
  CInputGroupText,
  CRow,
} from '@coreui/react'
import CIcon from '@coreui/icons-react'
// import FontAwesomeIcon from '@fortawesome/react-fontawesome'
import 'font-awesome/css/font-awesome.min.css'
import './Login.css'
import log from './img/log.svg'
import register from './img/register.svg'
// import { cilLockLocked, cilUser } from '@coreui/icons'
// const Login2 = React.lazy(() => import('./Login2'))
const Login = () => {
  const navigate = useNavigate()
  const [signIn, setSignIn] = useState('')
  const [signInUsername, setSignInUsername] = useState('')
  const [signInPassword, setSignInPassword] = useState('')
  const [errorMessage, setErrorMessage] = useState('')
  const [errorClass, setErrorClass] = useState('')
  const [shwMessage, setShwMessage] = useState(false)
  const onSigninUsernameChange = (evt) => {
    setSignInUsername(evt.target.value)
  }
  const onSigninPasswordChange = (evt) => {
    setSignInPassword(evt.target.value)
  }
  const onSigninSubmit = async (evt) => {
    evt.preventDefault()
    const form = evt.currentTarget
    setShwMessage(true)
    if (form.checkValidity() === false) {
      evt.stopPropagation()
    }
    let endPoint = 'http://127.0.0.1:8000/api/login'
    const data = { email: signInUsername, password: signInPassword }
    //console.log(data)

    const options = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    }
    let result = await fetch(endPoint, options)
    result = await result.json()
    console.log(result)
    if (result.status === '200') {
      navigate('/Dashboard')
    } else if (result.status === '420') {
      setErrorClass('alert alert-danger')
      setErrorMessage(result.message)
    }
  }
  return (
    <CContainer className={`${signIn}`}>
      <div className="forms-container">
        <div className="signin-signup">
          <CForm
            className="sign-in-form needs-validation"
            noValidate
            validated={shwMessage}
            onSubmit={onSigninSubmit}
          >
            <h2 className="title">Sign in</h2>
            {/* <div className="input-field">
              <i className="fa fa-user"></i>
              <input type="text" placeholder="Username" onChange={onSigninUsernameChange} />
            </div> */}
            <CCol md={8} className="position-relative input-field">
              <i className="fa fa-user"></i>
              <CFormInput
                type="email"
                id="validationTooltip02"
                required
                placeholder="Username"
                onChange={onSigninUsernameChange}
              />
              <CFormFeedback tooltip invalid>
                Please fill a valid email
              </CFormFeedback>
            </CCol>
            {/* <div className="input-field">
              <i className="fa fa-lock"></i>
              <input type="password" placeholder="Password" onChange={onSigninPasswordChange} />
            </div> */}
            <CCol md={8} className="position-relative input-field">
              <i className="fa fa-lock"></i>
              <CFormInput
                type="password"
                id="validationTooltip02"
                required
                placeholder="Password"
                onChange={onSigninPasswordChange}
              />
              <CFormFeedback tooltip invalid>
                Please enter a valid password
              </CFormFeedback>
            </CCol>
            {/* <Link to="/dashboard"> */}
            <CButton color="info" className="px-4" type="submit">
              Sign in
            </CButton>
            <div className={`${errorClass}`}>{errorMessage}</div>
            {/* </Link> */}
          </CForm>
          <CForm action="#" className="sign-up-form">
            <h2 className="title">Sign up</h2>
            <div className="input-field">
              <i className="fa fa-user"></i>
              <input type="text" placeholder="Name" />
            </div>
            <div className="input-field">
              <i className="fa fa-envelope"></i>
              <input type="email" placeholder="Email" />
            </div>
            <div className="input-field">
              <i className="fa fa-lock"></i>
              <input type="password" placeholder="Password" />
            </div>
            <div className="input-field">
              <i className="fa fa-lock"></i>
              <input type="password" placeholder="Confirm Password" />
            </div>
            <CButton color="info" className="px-4">
              Sign Up
            </CButton>
          </CForm>
        </div>
      </div>

      <div className="panels-container">
        <div className="panel left-panel">
          <div className="content">
            <h3>New here ?</h3>
            <p>Welcome, Kindly register yourself if you don&apos;t already have an account</p>
            <CButton
              className="btn transparent"
              id="sign-up-btn"
              onClick={() => {
                setSignIn('sign-up-mode')
              }}
            >
              Sign up
            </CButton>
          </div>
          <img src={log} className="image" alt="" />
        </div>
        <div className="panel right-panel">
          <div className="content">
            <h3>One of us ?</h3>
            <p>Kindly, fill out and login with your details</p>
            <CButton
              className="btn transparent"
              id="sign-in-btn"
              onClick={() => {
                setSignIn('')
              }}
            >
              Sign in
            </CButton>
          </div>
          <img src={register} className="image" alt="" />
        </div>
      </div>
    </CContainer>
  )
}

export default Login
