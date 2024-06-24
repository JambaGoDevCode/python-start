import asyncio

class ListenerRegister(object):
    def __init__(self):
        self._register = {}
        self._catch_alls = set()
        self._observers = {}

    def add_listener(self, event, listener):
        event = event.upper()
        listeners = self._register.get(event, set())
        listeners.add(listener)
        self._register[event] = listeners

    def add_catch_all_listener(self, listener):
        self._catch_alls.add(listener)

    def auto_listen(self, observer, prefix="_on_"):
        self._observers[observer] = prefix

    def remove_listener(self, event, listener):
        event = event.upper()
        listeners = self._register.get(event, None)
        if listeners:
            listeners.remove(listener)

    def remove_catch_all_listener(self, listener):
        self._catch_alls.remove(listener)

    def remove_event(self, event):
        event = event.upper()
        del self._register[event]

    def get_listeners(self, event):
        event = event.upper()
        return self._register.get(event, set())

    def get_catch_all_listeners(self):
        return self._catch_alls


class AsyncEventSource(ListenerRegister):
    def __init__(self):
        super(AsyncEventSource, self).__init__()

    @asyncio.coroutine
    def fire(self, event, *args, **kwargs):
        for each in self.get_listeners(event):
            yield from each(*args, **kwargs)

        for observer, prefix in self._observers.items():
            l = getattr(observer, prefix + str(event).lower(), False)
            if l and callable(l):
                yield from l(*args, **kwargs)

        for each in self.get_catch_all_listeners():
            yield from each(event, *args, **kwargs)


class EventSource(ListenerRegister):
    def __init__(self):
        super(EventSource, self).__init__()

    def fire(self, event, *args, **kwargs):
        for each in self.get_listeners(event):
            each(*args, **kwargs)

        for observer, prefix in self._observers.items():
            l = getattr(observer, prefix + str(event).lower(), False)
            if l and callable(l):
                l(*args, **kwargs)

        for each in self.get_catch_all_listeners():
            each(event, *args, **kwargs)


class TestClass(AsyncEventSource):
    def __init__(self):
        super(TestClass, self).__init__()
        print("ready")

    def event_occurs(self):
        # parameters for fire are 'event name' followed by anything you want to pass to the listener
        yield from self.fire("big bang event", "what a blast!")
        yield from self.fire("unknown", "Something")

    @asyncio.coroutine
    def simple_listener(self, payload):
        yield from asyncio.sleep(6)
        print("Payload : {0}".format(payload))

    @asyncio.coroutine
    def catchy(self, event_name, payload):
        yield from asyncio.sleep(3)
        print('Caught event {}: {}'.format(event_name, payload))


def demo():
    t = TestClass()

    # takes an event (any valid python object) and a listener (any valid python function)
    t.add_listener("big bang event", t.simple_listener)

    t.add_catch_all_listener(t.catchy)
    yield from t.event_occurs()  # when the event is fired in this method, the listener is informed


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(demo())
