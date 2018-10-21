module.exports = function open (link) {
  $$.html(`
    <iframe src="${link}" width="900" height="600"></iframe><br>
    <a href="${link}" style="margin: 20px 0">Open in StatSim</a>
  `)
}
