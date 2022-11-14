"""Count the diff summary."""


def count_summary(technology, diffs):
    """
    Count diffs summary for technology.

    Args:
        technology: string
        diffs: dict

    Returns:
        dict
    """
    inconsistencies_count = 0
    summary_by_nodes = []

    for node, cells in diffs.items():
        node_inconsistencies_count = len(cells)
        inconsistencies_count += node_inconsistencies_count
        summary_by_nodes.append({
            'node': node,
            'count': node_inconsistencies_count,
        })

    return (
        {
            'technology': technology,
            'count': inconsistencies_count,
        },
        sorted(summary_by_nodes, key=lambda element: element['count'], reverse=True),
    )


def get_summary(**diffs):
    """
    Prepare diffs summary for all technologies.

    Args:
        diffs: dict

    Returns:
        dict
    """
    summary = {
        'summary': [],
        'technology_details': [],
    }

    for technology, tech_diffs in diffs.items():
        tech_summary, summary_by_nodes = count_summary(technology, tech_diffs)
        summary['summary'].append(tech_summary)
        summary['technology_details'].append({
            'technology': technology,
            'summary_by_nodes': summary_by_nodes,
        })

    return summary
