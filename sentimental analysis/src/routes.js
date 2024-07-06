import React from 'react'

const AmazonForm = React.lazy(() => import('./views/AnalysSentiments/amazonforms/AmazonForm'))
const Dashboard = React.lazy(() => import('./views/dashboard/Dashboard'))
// const Dashboard = React.lazy(() => import('./views/dashboard/Dashboard'))
const TwitterForm = React.lazy(() => import('./views/AnalysSentiments/twitterforms/TwitterForm'))
const CriminalForm = React.lazy(() => import('./views/AnalysSentiments/criminalforms/CriminalForm'))
const routes = [
  { path: '/Home', exact: true, name: 'Home', element: Dashboard },
  { path: '/dashboard', name: 'Dashboard', element: Dashboard },
  { path: '/AnalysSentiments', name: 'Analys Sentiments', element: Dashboard, exact: true },
  { path: '/AnalysSentiments/amazonforms', name: 'Amazon Reviews', element: AmazonForm },
  { path: '/AnalysSentiments/twitterforms', name: 'Twitter tweets', element: TwitterForm },
  { path: '/AnalysSentiments/criminalforms', name: 'Criminal Activites', element: CriminalForm },
]
export default routes
