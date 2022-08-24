# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from hrs_project/MoveJointsRequest.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class MoveJointsRequest(genpy.Message):
  _md5sum = "83ee43bf529a242f799bbf5126b68060"
  _type = "hrs_project/MoveJointsRequest"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """
string joint_name
string end_effector
float64[] goal_6Dposition_Marker
float64[] goal_6Dposition_Cloth
float64[] goal_6Dposition

float64 SpeedorTime
float64 axisMask
int8 control_mod
bool getMarker
bool getMarker_Ground

string cloth_color
"""
  __slots__ = ['joint_name','end_effector','goal_6Dposition_Marker','goal_6Dposition_Cloth','goal_6Dposition','SpeedorTime','axisMask','control_mod','getMarker','getMarker_Ground','cloth_color']
  _slot_types = ['string','string','float64[]','float64[]','float64[]','float64','float64','int8','bool','bool','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       joint_name,end_effector,goal_6Dposition_Marker,goal_6Dposition_Cloth,goal_6Dposition,SpeedorTime,axisMask,control_mod,getMarker,getMarker_Ground,cloth_color

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(MoveJointsRequest, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.joint_name is None:
        self.joint_name = ''
      if self.end_effector is None:
        self.end_effector = ''
      if self.goal_6Dposition_Marker is None:
        self.goal_6Dposition_Marker = []
      if self.goal_6Dposition_Cloth is None:
        self.goal_6Dposition_Cloth = []
      if self.goal_6Dposition is None:
        self.goal_6Dposition = []
      if self.SpeedorTime is None:
        self.SpeedorTime = 0.
      if self.axisMask is None:
        self.axisMask = 0.
      if self.control_mod is None:
        self.control_mod = 0
      if self.getMarker is None:
        self.getMarker = False
      if self.getMarker_Ground is None:
        self.getMarker_Ground = False
      if self.cloth_color is None:
        self.cloth_color = ''
    else:
      self.joint_name = ''
      self.end_effector = ''
      self.goal_6Dposition_Marker = []
      self.goal_6Dposition_Cloth = []
      self.goal_6Dposition = []
      self.SpeedorTime = 0.
      self.axisMask = 0.
      self.control_mod = 0
      self.getMarker = False
      self.getMarker_Ground = False
      self.cloth_color = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.joint_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.end_effector
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.goal_6Dposition_Marker)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.goal_6Dposition_Marker))
      length = len(self.goal_6Dposition_Cloth)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.goal_6Dposition_Cloth))
      length = len(self.goal_6Dposition)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.goal_6Dposition))
      _x = self
      buff.write(_get_struct_2db2B().pack(_x.SpeedorTime, _x.axisMask, _x.control_mod, _x.getMarker, _x.getMarker_Ground))
      _x = self.cloth_color
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.joint_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.joint_name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.end_effector = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.end_effector = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.goal_6Dposition_Marker = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.goal_6Dposition_Cloth = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.goal_6Dposition = s.unpack(str[start:end])
      _x = self
      start = end
      end += 19
      (_x.SpeedorTime, _x.axisMask, _x.control_mod, _x.getMarker, _x.getMarker_Ground,) = _get_struct_2db2B().unpack(str[start:end])
      self.getMarker = bool(self.getMarker)
      self.getMarker_Ground = bool(self.getMarker_Ground)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.cloth_color = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.cloth_color = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.joint_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.end_effector
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.goal_6Dposition_Marker)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.goal_6Dposition_Marker.tostring())
      length = len(self.goal_6Dposition_Cloth)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.goal_6Dposition_Cloth.tostring())
      length = len(self.goal_6Dposition)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.goal_6Dposition.tostring())
      _x = self
      buff.write(_get_struct_2db2B().pack(_x.SpeedorTime, _x.axisMask, _x.control_mod, _x.getMarker, _x.getMarker_Ground))
      _x = self.cloth_color
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.joint_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.joint_name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.end_effector = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.end_effector = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.goal_6Dposition_Marker = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.goal_6Dposition_Cloth = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.goal_6Dposition = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      _x = self
      start = end
      end += 19
      (_x.SpeedorTime, _x.axisMask, _x.control_mod, _x.getMarker, _x.getMarker_Ground,) = _get_struct_2db2B().unpack(str[start:end])
      self.getMarker = bool(self.getMarker)
      self.getMarker_Ground = bool(self.getMarker_Ground)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.cloth_color = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.cloth_color = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2db2B = None
def _get_struct_2db2B():
    global _struct_2db2B
    if _struct_2db2B is None:
        _struct_2db2B = struct.Struct("<2db2B")
    return _struct_2db2B
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from hrs_project/MoveJointsResponse.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class MoveJointsResponse(genpy.Message):
  _md5sum = "ba6f0325e3a676f603e6569a23450230"
  _type = "hrs_project/MoveJointsResponse"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """

float64 num
bool RosePick_Ready
bool bMarkerArrived
string speechCommand


"""
  __slots__ = ['num','RosePick_Ready','bMarkerArrived','speechCommand']
  _slot_types = ['float64','bool','bool','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       num,RosePick_Ready,bMarkerArrived,speechCommand

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(MoveJointsResponse, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.num is None:
        self.num = 0.
      if self.RosePick_Ready is None:
        self.RosePick_Ready = False
      if self.bMarkerArrived is None:
        self.bMarkerArrived = False
      if self.speechCommand is None:
        self.speechCommand = ''
    else:
      self.num = 0.
      self.RosePick_Ready = False
      self.bMarkerArrived = False
      self.speechCommand = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_d2B().pack(_x.num, _x.RosePick_Ready, _x.bMarkerArrived))
      _x = self.speechCommand
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 10
      (_x.num, _x.RosePick_Ready, _x.bMarkerArrived,) = _get_struct_d2B().unpack(str[start:end])
      self.RosePick_Ready = bool(self.RosePick_Ready)
      self.bMarkerArrived = bool(self.bMarkerArrived)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.speechCommand = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.speechCommand = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_d2B().pack(_x.num, _x.RosePick_Ready, _x.bMarkerArrived))
      _x = self.speechCommand
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 10
      (_x.num, _x.RosePick_Ready, _x.bMarkerArrived,) = _get_struct_d2B().unpack(str[start:end])
      self.RosePick_Ready = bool(self.RosePick_Ready)
      self.bMarkerArrived = bool(self.bMarkerArrived)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.speechCommand = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.speechCommand = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_d2B = None
def _get_struct_d2B():
    global _struct_d2B
    if _struct_d2B is None:
        _struct_d2B = struct.Struct("<d2B")
    return _struct_d2B
class MoveJoints(object):
  _type          = 'hrs_project/MoveJoints'
  _md5sum = '904bb3e81ce1f0698f6188c53777d573'
  _request_class  = MoveJointsRequest
  _response_class = MoveJointsResponse