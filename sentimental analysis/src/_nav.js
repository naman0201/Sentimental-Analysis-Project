import React from 'react'
import CIcon from '@coreui/icons-react'
import {
  cilBell,
  cilCalculator,
  cilChartPie,
  cilCursor,
  cilDrop,
  cilNotes,
  cilPencil,
  cilPuzzle,
  cilSpeedometer,
  cibTwitter,
  cibAmazon,
  cibRedditAlt,
} from '@coreui/icons'
import { CNavGroup, CNavItem, CNavTitle } from '@coreui/react'

const _nav = [
  {
    component: CNavItem,
    name: 'Dashboard',
    to: '/dashboard',
    icon: <CIcon icon={cilSpeedometer} customClassName="nav-icon" />,
  },
  {
    component: CNavGroup,
    name: 'Analys Sentiments',
    to: '/base',
    icon: <CIcon icon={cilPuzzle} customClassName="nav-icon" />,
    items: [
      {
        component: CNavItem,
        name: 'Ecommerce Reviews',
        to: '/AnalysSentiments/amazonforms',
        icon: <CIcon icon={cibAmazon} customClassName="nav-icon" />,
      },
      {
        component: CNavItem,
        name: 'Twitter tweets',
        to: '/AnalysSentiments/twitterforms',
        icon: <CIcon icon={cibTwitter} customClassName="nav-icon" />,
      },
      {
        component: CNavItem,
        name: 'Criminals activities',
        to: '/AnalysSentiments/criminalforms',
        icon: <CIcon icon={cibRedditAlt} customClassName="nav-icon" />,
      },
    ],
  },
]

export default _nav
