// Generated by gencpp from file hrs_project/SetSpeechVocabularyFeedback.msg
// DO NOT EDIT!


#ifndef HRS_PROJECT_MESSAGE_SETSPEECHVOCABULARYFEEDBACK_H
#define HRS_PROJECT_MESSAGE_SETSPEECHVOCABULARYFEEDBACK_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace hrs_project
{
template <class ContainerAllocator>
struct SetSpeechVocabularyFeedback_
{
  typedef SetSpeechVocabularyFeedback_<ContainerAllocator> Type;

  SetSpeechVocabularyFeedback_()
    {
    }
  SetSpeechVocabularyFeedback_(const ContainerAllocator& _alloc)
    {
  (void)_alloc;
    }







  typedef boost::shared_ptr< ::hrs_project::SetSpeechVocabularyFeedback_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::hrs_project::SetSpeechVocabularyFeedback_<ContainerAllocator> const> ConstPtr;

}; // struct SetSpeechVocabularyFeedback_

typedef ::hrs_project::SetSpeechVocabularyFeedback_<std::allocator<void> > SetSpeechVocabularyFeedback;

typedef boost::shared_ptr< ::hrs_project::SetSpeechVocabularyFeedback > SetSpeechVocabularyFeedbackPtr;
typedef boost::shared_ptr< ::hrs_project::SetSpeechVocabularyFeedback const> SetSpeechVocabularyFeedbackConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::hrs_project::SetSpeechVocabularyFeedback_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::hrs_project::SetSpeechVocabularyFeedback_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace hrs_project

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg'], 'hrs_project': ['/home/nao_a/ros/hrs_project/devel/.private/hrs_project/share/hrs_project/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::hrs_project::SetSpeechVocabularyFeedback_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::hrs_project::SetSpeechVocabularyFeedback_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::hrs_project::SetSpeechVocabularyFeedback_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::hrs_project::SetSpeechVocabularyFeedback_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::hrs_project::SetSpeechVocabularyFeedback_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::hrs_project::SetSpeechVocabularyFeedback_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::hrs_project::SetSpeechVocabularyFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const ::hrs_project::SetSpeechVocabularyFeedback_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::hrs_project::SetSpeechVocabularyFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "hrs_project/SetSpeechVocabularyFeedback";
  }

  static const char* value(const ::hrs_project::SetSpeechVocabularyFeedback_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::hrs_project::SetSpeechVocabularyFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
\n\
\n\
";
  }

  static const char* value(const ::hrs_project::SetSpeechVocabularyFeedback_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::hrs_project::SetSpeechVocabularyFeedback_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream&, T)
    {}

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SetSpeechVocabularyFeedback_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::hrs_project::SetSpeechVocabularyFeedback_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream&, const std::string&, const ::hrs_project::SetSpeechVocabularyFeedback_<ContainerAllocator>&)
  {}
};

} // namespace message_operations
} // namespace ros

#endif // HRS_PROJECT_MESSAGE_SETSPEECHVOCABULARYFEEDBACK_H
