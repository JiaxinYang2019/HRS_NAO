;; Auto-generated. Do not edit!


(when (boundp 'hrs_project::SpeechWithFeedbackGoal)
  (if (not (find-package "HRS_PROJECT"))
    (make-package "HRS_PROJECT"))
  (shadow 'SpeechWithFeedbackGoal (find-package "HRS_PROJECT")))
(unless (find-package "HRS_PROJECT::SPEECHWITHFEEDBACKGOAL")
  (make-package "HRS_PROJECT::SPEECHWITHFEEDBACKGOAL"))

(in-package "ROS")
;;//! \htmlinclude SpeechWithFeedbackGoal.msg.html


(defclass hrs_project::SpeechWithFeedbackGoal
  :super ros::object
  :slots (_say ))

(defmethod hrs_project::SpeechWithFeedbackGoal
  (:init
   (&key
    ((:say __say) "")
    )
   (send-super :init)
   (setq _say (string __say))
   self)
  (:say
   (&optional __say)
   (if __say (setq _say __say)) _say)
  (:serialization-length
   ()
   (+
    ;; string _say
    4 (length _say)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _say
       (write-long (length _say) s) (princ _say s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _say
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _say (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get hrs_project::SpeechWithFeedbackGoal :md5sum-) "331898fd34308d7c3706d43ca7f6e377")
(setf (get hrs_project::SpeechWithFeedbackGoal :datatype-) "hrs_project/SpeechWithFeedbackGoal")
(setf (get hrs_project::SpeechWithFeedbackGoal :definition-)
      "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
# Purpose : To have feedback on when the speech was started and when 
# NAO stopped talking
# Goal: The sentence for NAO to say 
# Result: NAO has finished speaking
# Feedback: When NAO starts speaking

string say

")



(provide :hrs_project/SpeechWithFeedbackGoal "331898fd34308d7c3706d43ca7f6e377")

