// exportUtils.js

export function exportCSV(data, filename) {
  const csv = data.map(row => row.join(',')).join('\n')
  const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' })
  const url = URL.createObjectURL(blob)
  const link = document.createElement('a')

  link.setAttribute('href', url)
  link.setAttribute('download', filename)
  document.body.appendChild(link)
  link.click()
}

export function exportPDF(data, filename) {
  // Implement PDF export logic using jsPDF here
  // Add content to the PDF, format it, and save or trigger download
}
