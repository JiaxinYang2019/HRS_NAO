;; Auto-generated. Do not edit!


(when (boundp 'hrs_project::SetSpeechVocabularyFeedback)
  (if (not (find-package "HRS_PROJECT"))
    (make-package "HRS_PROJECT"))
  (shadow 'SetSpeechVocabularyFeedback (find-package "HRS_PROJECT")))
(unless (find-package "HRS_PROJECT::SETSPEECHVOCABULARYFEEDBACK")
  (make-package "HRS_PROJECT::SETSPEECHVOCABULARYFEEDBACK"))

(in-package "ROS")
;;//! \htmlinclude SetSpeechVocabularyFeedback.msg.html


(defclass hrs_project::SetSpeechVocabularyFeedback
  :super ros::object
  :slots ())

(defmethod hrs_project::SetSpeechVocabularyFeedback
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(setf (get hrs_project::SetSpeechVocabularyFeedback :md5sum-) "d41d8cd98f00b204e9800998ecf8427e")
(setf (get hrs_project::SetSpeechVocabularyFeedback :datatype-) "hrs_project/SetSpeechVocabularyFeedback")
(setf (get hrs_project::SetSpeechVocabularyFeedback :definition-)
      "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======



")



(provide :hrs_project/SetSpeechVocabularyFeedback "d41d8cd98f00b204e9800998ecf8427e")


