from collections import Counter
from model import Event


class EventFormatter:

    def format_events(self, events: list[Event]) -> tuple[str, ...]:
        push_counts = self._count_push_events(events)

        formatters = {
            "PushEvent": self._format_push_event,
            "CreateEvent": self._format_create_event,
        }

        formatted_events = []
        processed_pushes = set()

        for event in events:
            formatter = formatters.get(event.event_type)

            if formatter is None:
                formatted_events.append(
                    f"Unsupported event type: {event.event_type}"
                )
                continue

            if event.event_type == "PushEvent":
                repository_id = event.payload.repository_id

                if repository_id in processed_pushes:
                    continue

                processed_pushes.add(repository_id)

            formatted_events.append(
                formatter(event, push_counts)
            )

        return tuple(formatted_events)
    

    @staticmethod
    def _count_push_events(events: list[Event]) -> Counter:
        return Counter(
            event.payload.repository_id
            for event in events
            if event.event_type == "PushEvent"
        )
        
    
    @staticmethod
    def _format_create_event(
        event: Event,
        push_counts: Counter,
    ) -> str:
        return (
            f"Created {event.payload.ref_type} "
            f"{event.payload.ref} in {event.repo.name}"
        )
    
    
    @staticmethod
    def _format_push_event(
        event: Event,
        push_counts: Counter,
    ) -> str:
        push_count = push_counts[event.payload.repository_id]

        return (
            f"Pushed {push_count} commits "
            f"to {event.repo.name}"
        )