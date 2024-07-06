import React from 'react'
import {
  CButton,
  CCard,
  CCardBody,
  CCardFooter,
  CCardGroup,
  CCardHeader,
  CCardImage,
  CCardLink,
  CCardSubtitle,
  CCardText,
  CCardTitle,
  CListGroup,
  CListGroupItem,
  CNav,
  CNavItem,
  CNavLink,
  CCol,
  CRow,
} from '@coreui/react'
import { DocsExample } from 'src/components'
import { Link } from 'react-router-dom'
import AmazonImg from 'src/assets/images/amazon.jpg'
import TwitterImg from 'src/assets/images/twitter.png'
import CriminalImg from 'src/assets/images/criminal.jpg'
const Cards = () => {
  return (
    <CRow>
      <CCol xs={12}>
        <CCard className="mb-4">
          <CCardBody>
            <DocsExample href="components/card/#grid-cards">
              <CRow xs={{ cols: 1, gutter: 4 }} md={{ cols: 3 }}>
                {[
                  {
                    color: 'warning',
                    imgsrc: AmazonImg,
                    title: 'Amazon',
                    desc: 'This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.',
                    handler: '/AnalysSentiments/amazonforms',
                  },
                  {
                    color: 'info',
                    imgsrc: TwitterImg,
                    title: 'Twitter',
                    desc: 'This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.',
                    handler: '/AnalysSentiments/twitterforms',
                  },
                  {
                    color: 'danger',
                    imgsrc: CriminalImg,
                    title: 'Criminal',
                    desc: 'This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.',
                    handler: '/AnalysSentiments/criminalforms',
                  },
                ].map((item, index) => (
                  <CCol key={index}>
                    <Link to={item.handler} className="text-decoration-none">
                      <CCard color={item.color} textColor="white">
                        <CCardImage orientation="top" src={item.imgsrc} />
                        <CCardBody>
                          <CCardTitle className="text-decoration-none">{item.title}</CCardTitle>
                          <CCardText>{item.desc}</CCardText>
                        </CCardBody>
                      </CCard>
                    </Link>
                  </CCol>
                ))}
              </CRow>
            </DocsExample>
          </CCardBody>
        </CCard>
      </CCol>
    </CRow>
  )
}

export default Cards
