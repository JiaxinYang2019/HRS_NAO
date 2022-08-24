; Auto-generated. Do not edit!


(cl:in-package hrs_project-msg)


;//! \htmlinclude SetSpeechVocabularyActionFeedback.msg.html

(cl:defclass <SetSpeechVocabularyActionFeedback> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (status
    :reader status
    :initarg :status
    :type actionlib_msgs-msg:GoalStatus
    :initform (cl:make-instance 'actionlib_msgs-msg:GoalStatus))
   (feedback
    :reader feedback
    :initarg :feedback
    :type hrs_project-msg:SetSpeechVocabularyFeedback
    :initform (cl:make-instance 'hrs_project-msg:SetSpeechVocabularyFeedback)))
)

(cl:defclass SetSpeechVocabularyActionFeedback (<SetSpeechVocabularyActionFeedback>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetSpeechVocabularyActionFeedback>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetSpeechVocabularyActionFeedback)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name hrs_project-msg:<SetSpeechVocabularyActionFeedback> is deprecated: use hrs_project-msg:SetSpeechVocabularyActionFeedback instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <SetSpeechVocabularyActionFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hrs_project-msg:header-val is deprecated.  Use hrs_project-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <SetSpeechVocabularyActionFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hrs_project-msg:status-val is deprecated.  Use hrs_project-msg:status instead.")
  (status m))

(cl:ensure-generic-function 'feedback-val :lambda-list '(m))
(cl:defmethod feedback-val ((m <SetSpeechVocabularyActionFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hrs_project-msg:feedback-val is deprecated.  Use hrs_project-msg:feedback instead.")
  (feedback m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetSpeechVocabularyActionFeedback>) ostream)
  "Serializes a message object of type '<SetSpeechVocabularyActionFeedback>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'status) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'feedback) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetSpeechVocabularyActionFeedback>) istream)
  "Deserializes a message object of type '<SetSpeechVocabularyActionFeedback>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'status) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'feedback) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetSpeechVocabularyActionFeedback>)))
  "Returns string type for a message object of type '<SetSpeechVocabularyActionFeedback>"
  "hrs_project/SetSpeechVocabularyActionFeedback")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetSpeechVocabularyActionFeedback)))
  "Returns string type for a message object of type 'SetSpeechVocabularyActionFeedback"
  "hrs_project/SetSpeechVocabularyActionFeedback")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetSpeechVocabularyActionFeedback>)))
  "Returns md5sum for a message object of type '<SetSpeechVocabularyActionFeedback>"
  "aae20e09065c3809e8a8e87c4c8953fd")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetSpeechVocabularyActionFeedback)))
  "Returns md5sum for a message object of type 'SetSpeechVocabularyActionFeedback"
  "aae20e09065c3809e8a8e87c4c8953fd")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetSpeechVocabularyActionFeedback>)))
  "Returns full string definition for message of type '<SetSpeechVocabularyActionFeedback>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalStatus status~%SetSpeechVocabularyFeedback feedback~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: actionlib_msgs/GoalStatus~%GoalID goal_id~%uint8 status~%uint8 PENDING         = 0   # The goal has yet to be processed by the action server~%uint8 ACTIVE          = 1   # The goal is currently being processed by the action server~%uint8 PREEMPTED       = 2   # The goal received a cancel request after it started executing~%                            #   and has since completed its execution (Terminal State)~%uint8 SUCCEEDED       = 3   # The goal was achieved successfully by the action server (Terminal State)~%uint8 ABORTED         = 4   # The goal was aborted during execution by the action server due~%                            #    to some failure (Terminal State)~%uint8 REJECTED        = 5   # The goal was rejected by the action server without being processed,~%                            #    because the goal was unattainable or invalid (Terminal State)~%uint8 PREEMPTING      = 6   # The goal received a cancel request after it started executing~%                            #    and has not yet completed execution~%uint8 RECALLING       = 7   # The goal received a cancel request before it started executing,~%                            #    but the action server has not yet confirmed that the goal is canceled~%uint8 RECALLED        = 8   # The goal received a cancel request before it started executing~%                            #    and was successfully cancelled (Terminal State)~%uint8 LOST            = 9   # An action client can determine that a goal is LOST. This should not be~%                            #    sent over the wire by an action server~%~%#Allow for the user to associate a string with GoalStatus for debugging~%string text~%~%~%================================================================================~%MSG: actionlib_msgs/GoalID~%# The stamp should store the time at which this goal was requested.~%# It is used by an action server when it tries to preempt all~%# goals that were requested before a certain time~%time stamp~%~%# The id provides a way to associate feedback and~%# result message with specific goal requests. The id~%# specified must be unique.~%string id~%~%~%================================================================================~%MSG: hrs_project/SetSpeechVocabularyFeedback~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetSpeechVocabularyActionFeedback)))
  "Returns full string definition for message of type 'SetSpeechVocabularyActionFeedback"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalStatus status~%SetSpeechVocabularyFeedback feedback~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: actionlib_msgs/GoalStatus~%GoalID goal_id~%uint8 status~%uint8 PENDING         = 0   # The goal has yet to be processed by the action server~%uint8 ACTIVE          = 1   # The goal is currently being processed by the action server~%uint8 PREEMPTED       = 2   # The goal received a cancel request after it started executing~%                            #   and has since completed its execution (Terminal State)~%uint8 SUCCEEDED       = 3   # The goal was achieved successfully by the action server (Terminal State)~%uint8 ABORTED         = 4   # The goal was aborted during execution by the action server due~%                            #    to some failure (Terminal State)~%uint8 REJECTED        = 5   # The goal was rejected by the action server without being processed,~%                            #    because the goal was unattainable or invalid (Terminal State)~%uint8 PREEMPTING      = 6   # The goal received a cancel request after it started executing~%                            #    and has not yet completed execution~%uint8 RECALLING       = 7   # The goal received a cancel request before it started executing,~%                            #    but the action server has not yet confirmed that the goal is canceled~%uint8 RECALLED        = 8   # The goal received a cancel request before it started executing~%                            #    and was successfully cancelled (Terminal State)~%uint8 LOST            = 9   # An action client can determine that a goal is LOST. This should not be~%                            #    sent over the wire by an action server~%~%#Allow for the user to associate a string with GoalStatus for debugging~%string text~%~%~%================================================================================~%MSG: actionlib_msgs/GoalID~%# The stamp should store the time at which this goal was requested.~%# It is used by an action server when it tries to preempt all~%# goals that were requested before a certain time~%time stamp~%~%# The id provides a way to associate feedback and~%# result message with specific goal requests. The id~%# specified must be unique.~%string id~%~%~%================================================================================~%MSG: hrs_project/SetSpeechVocabularyFeedback~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetSpeechVocabularyActionFeedback>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'status))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'feedback))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetSpeechVocabularyActionFeedback>))
  "Converts a ROS message object to a list"
  (cl:list 'SetSpeechVocabularyActionFeedback
    (cl:cons ':header (header msg))
    (cl:cons ':status (status msg))
    (cl:cons ':feedback (feedback msg))
))
