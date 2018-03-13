// jshint ignore: start
/* More flexible Content loader pattern.
 *
 * Options:
 *    ajax_url(string): URL to load cytocape graph data from..
 *    trigger(string): Event to trigger content loading. Defaults to "immediate"
 *
 */

require([
  'jquery',
  'pat-base',
  'pat-logger',
  'pat-registry',
  'mockup-utils',
  'cytoscape',
  'cytoscape-cose-bilkent',
  'underscore',
], function($, Base, logger, Registry, utils, cytoscape, coseBilkent,  _) {
  'use strict';
  var log = logger.getLogger('pat-graph');
  console.log('pat-graph');

  var ContentLoader = Base.extend({
    name: 'graph',
    trigger: '.pat-graph',
    parser: 'mockup',
    defaults: {
      ajax_url: null,
      trigger: 'immediate',
      target: null,
      template: null,
      dataType: 'json',
      form_id: '',
      query_id: ''
    },
    init: function() {
      console.log('pat-graph: init');
      coseBilkent( cytoscape );
      coseBilkent( cytoscape );
      var that = this;
      if(that.options.trigger === 'immediate'){
        that._load();
      }else{
        that.$el.on(that.options.trigger, function(e){
          e.preventDefault();
          that._load();
        });
      }
    },
    _cytoscape: function(data){
      var that = this;
      var cy = cytoscape({
        container: $('#cy'), // container to render in
        elements: data['elements'],
        style: cytoscape.stylesheet()
            .selector('node')
              .css({
                'font-size': '10pt',
                'background-color': 'data(pkbackgroundcolor)',
                'shape': 'data(pkshape)',
                'width': 'data(pkwidth)',
                'content': 'data(title)',
                'text-halign': 'center',
                'text-valign': 'center',
                'height':'20',
                'border-color':'#000000',
              })
            .selector('edge')
              .css({
                'label': 'data(label)',
                'edge-text-rotation': 'autorotate'
              }),
        layout: {
        name: 'dagre',
//        idealEdgeLength: 500,
//        nodeOverlap: 2,
//        refresh: 20,
//        fit: true,
//        padding: 300,
//        randomize: true,
//        componentSpacing: 100,
//        nodeRepulsion: 4000000,
//        edgeElasticity: 10000,
//        nestingFactor: 1,
//        gravity: 2,
//        numIter: 5000,
//        initialTemp: 200,
//        coolingFactor: 0.98,
//        minTemp: 1.0,
//        tile: true,
//        animate: true,
//        tilingPaddingVertical: 80,
//        tilingPaddingHorizontal: 80
      }
        });
    },
    _load: function(){
      var that = this;
      that.$el.addClass('loading-content');
      if(that.options.ajax_url){
        that.loadRemote();
      }else{
        that.loadLocal();
      }
    },
    loadRemote: function(){
      var that = this;
      $.ajax({
        url: that.options.ajax_url,
        dataType: that.options.dataType,
        success: function(data){
          that._cytoscape(data);
        },
        error: function(){
          that.$el.addClass('content-load-error');
        }
      });
    },

  });

  return ContentLoader;

});
