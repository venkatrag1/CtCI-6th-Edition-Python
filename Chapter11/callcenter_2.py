import unittest

class Call(object):
    def __init__(self, issue):
        self.text = issue
        self.assignee = None

    def resolve(self, handled):
        if handled:
            self.issue = None
        self.assignee.finish_call(handled)

class Employee(object):
    def __init__(self, name, superior):
        self.name = name
        self.superior = superior
        self.call = None



class Test(unittest.TestCase):
  def test_call_center(self):
    lashaun = Director("Lashaun")
    juan = Manager("Juan", lashaun)
    sally = Manager("Sally", lashaun)
    boris = Respondent("Boris", juan)
    sam = Respondent("Sam", juan)
    jordan = Respondent("Jordan", sally)
    casey = Respondent("Casey", sally)
    center = CallCenter([boris, sam, jordan, casey], [juan, lashaun], sally)
    call1 = Call("The toilet")
    call2 = Call("The webpage")
    call3 = Call("The email")
    call4 = Call("The lizard")
    call5 = Call("The cloudy weather")
    call6 = Call("The noise")
    self.assertEqual(len(center.respondent_queue), 4)
    center.route_call(call1)
    center.route_call(call2)
    self.assertEqual(len(center.respondent_queue), 2)
    center.route_call(call3)
    center.route_call(call4)
    center.route_call(call5)
    center.route_call(call6)
    self.assertEqual(center.call_queue, [call5, call6])
    call1.resolve(True)
    self.assertEqual(call1.issue, None)
    self.assertEqual(center.call_queue, [call6])
    self.assertEqual(sally.call, None)
    self.assertEqual(lashaun.call, None)
    call4.resolve(False)
    self.assertEqual(sally.call, call4)
    call4.resolve(False)
    self.assertEqual(sally.call, None)
    self.assertEqual(lashaun.call, call4)
    call4.resolve(True)
    self.assertEqual(lashaun.call, None)
    call6.resolve(True)
    self.assertEqual(center.respondent_queue, [casey])

if __name__ == "__main__":
  unittest.main()