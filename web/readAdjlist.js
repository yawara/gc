adjlist="results/13.txt"

function readAdjlist(url){
  $.get(url,function(data,status){
    lines = data.split("\n")
    H = jsnx.emptyGraph()
    for( line of lines ){
      if( line[0] != "#" && line != "" ){
        nodes = line.split(" ")
        H.addNode(nodes[0])
        for ( node of nodes.slice(1) ){
          console.log(node)
          H.addNode(node)
          H.addEdge(nodes[0],node)
        }
      }
    }
    jsnx.draw(H, {
      element: "#demo-canvas",
      layoutAttr: {
        charge: -450,
        linkDistance: 200
      }
    })
  })
}

readAdjlist(adjlist)