"""
Those are helper tools that could help in applications' tests.
"""


def get_cell_count(widget, filter_function):
    """
    :param qmxgraph.widget.QmxGraph widget: The widget used to display the
        graph.
    :param str filter_function: A javascript function used to filter the
        cells.
    :rtype: int
    """
    count = widget.inner_web_view().eval_js('''(function(){{
        var all_cells = api._graphEditor.graph.model.cells;
        var cells = Object.keys(all_cells).map(
            function(id){{ return all_cells[id]; }}
        );

        cells = cells.filter({filter_func});
        return cells.length;
    }})()'''.format(filter_func=filter_function))
    return int(count)
