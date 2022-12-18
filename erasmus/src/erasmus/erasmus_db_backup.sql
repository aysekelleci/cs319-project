PGDMP     !                    z         	   erasmusdb    15.1    15.1    R           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            S           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            T           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            U           1262    16942 	   erasmusdb    DATABASE     }   CREATE DATABASE erasmusdb WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_Europe.1254';
    DROP DATABASE erasmusdb;
                postgres    false            �            1259    17138    accounts_boardmember    TABLE     b   CREATE TABLE public.accounts_boardmember (
    id bigint NOT NULL,
    user_id bigint NOT NULL
);
 (   DROP TABLE public.accounts_boardmember;
       public         heap    postgres    false            �            1259    17137    accounts_boardmember_id_seq    SEQUENCE     �   CREATE SEQUENCE public.accounts_boardmember_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.accounts_boardmember_id_seq;
       public          postgres    false    243            V           0    0    accounts_boardmember_id_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public.accounts_boardmember_id_seq OWNED BY public.accounts_boardmember.id;
          public          postgres    false    242            �            1259    17129    accounts_coordinator    TABLE     b   CREATE TABLE public.accounts_coordinator (
    id bigint NOT NULL,
    user_id bigint NOT NULL
);
 (   DROP TABLE public.accounts_coordinator;
       public         heap    postgres    false            �            1259    17128    accounts_coordinator_id_seq    SEQUENCE     �   CREATE SEQUENCE public.accounts_coordinator_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.accounts_coordinator_id_seq;
       public          postgres    false    241            W           0    0    accounts_coordinator_id_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public.accounts_coordinator_id_seq OWNED BY public.accounts_coordinator.id;
          public          postgres    false    240            �            1259    17106    accounts_erasmususer    TABLE     %  CREATE TABLE public.accounts_erasmususer (
    id bigint NOT NULL,
    email character varying(100) NOT NULL,
    bilkent_id integer NOT NULL,
    phone integer NOT NULL,
    user_id integer NOT NULL,
    name character varying(100) NOT NULL,
    department character varying(100) NOT NULL
);
 (   DROP TABLE public.accounts_erasmususer;
       public         heap    postgres    false            �            1259    17105    accounts_erasmususer_id_seq    SEQUENCE     �   CREATE SEQUENCE public.accounts_erasmususer_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.accounts_erasmususer_id_seq;
       public          postgres    false    237            X           0    0    accounts_erasmususer_id_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public.accounts_erasmususer_id_seq OWNED BY public.accounts_erasmususer.id;
          public          postgres    false    236            �            1259    17120    accounts_student    TABLE     U  CREATE TABLE public.accounts_student (
    id bigint NOT NULL,
    gpa double precision NOT NULL,
    score double precision NOT NULL,
    status character varying(200) NOT NULL,
    is_erasmus_done boolean NOT NULL,
    user_id bigint NOT NULL,
    coordinator_id bigint,
    academic_year character varying(20) NOT NULL,
    semester character varying(20) NOT NULL,
    university_id bigint,
    email_visibility boolean NOT NULL,
    mobility_visiblity boolean NOT NULL,
    phone_visibility boolean NOT NULL,
    status_visibility boolean NOT NULL,
    final_list_approved boolean NOT NULL
);
 $   DROP TABLE public.accounts_student;
       public         heap    postgres    false            �            1259    17119    accounts_student_id_seq    SEQUENCE     �   CREATE SEQUENCE public.accounts_student_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.accounts_student_id_seq;
       public          postgres    false    239            Y           0    0    accounts_student_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.accounts_student_id_seq OWNED BY public.accounts_student.id;
          public          postgres    false    238            �            1259    17181    accounts_todo    TABLE     A  CREATE TABLE public.accounts_todo (
    id bigint NOT NULL,
    header character varying(100) NOT NULL,
    body character varying(400) NOT NULL,
    link character varying(200) NOT NULL,
    is_flagged boolean NOT NULL,
    is_done boolean NOT NULL,
    due_date timestamp with time zone,
    user_id bigint NOT NULL
);
 !   DROP TABLE public.accounts_todo;
       public         heap    postgres    false            �            1259    17180    accounts_todo_id_seq    SEQUENCE     }   CREATE SEQUENCE public.accounts_todo_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.accounts_todo_id_seq;
       public          postgres    false    247            Z           0    0    accounts_todo_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.accounts_todo_id_seq OWNED BY public.accounts_todo.id;
          public          postgres    false    246            �            1259    17162    accounts_usercourse    TABLE     �   CREATE TABLE public.accounts_usercourse (
    id bigint NOT NULL,
    grade integer,
    course_id bigint NOT NULL,
    user_id bigint NOT NULL,
    submitted boolean NOT NULL
);
 '   DROP TABLE public.accounts_usercourse;
       public         heap    postgres    false            �            1259    17161    accounts_usercourse_id_seq    SEQUENCE     �   CREATE SEQUENCE public.accounts_usercourse_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.accounts_usercourse_id_seq;
       public          postgres    false    245            [           0    0    accounts_usercourse_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.accounts_usercourse_id_seq OWNED BY public.accounts_usercourse.id;
          public          postgres    false    244            �            1259    17015 
   auth_group    TABLE     f   CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);
    DROP TABLE public.auth_group;
       public         heap    postgres    false            �            1259    17014    auth_group_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.auth_group_id_seq;
       public          postgres    false    227            \           0    0    auth_group_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;
          public          postgres    false    226            �            1259    17024    auth_group_permissions    TABLE     �   CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);
 *   DROP TABLE public.auth_group_permissions;
       public         heap    postgres    false            �            1259    17023    auth_group_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.auth_group_permissions_id_seq;
       public          postgres    false    229            ]           0    0    auth_group_permissions_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;
          public          postgres    false    228            �            1259    17008    auth_permission    TABLE     �   CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);
 #   DROP TABLE public.auth_permission;
       public         heap    postgres    false            �            1259    17007    auth_permission_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.auth_permission_id_seq;
       public          postgres    false    225            ^           0    0    auth_permission_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;
          public          postgres    false    224            �            1259    17031 	   auth_user    TABLE     �  CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);
    DROP TABLE public.auth_user;
       public         heap    postgres    false            �            1259    17040    auth_user_groups    TABLE     ~   CREATE TABLE public.auth_user_groups (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);
 $   DROP TABLE public.auth_user_groups;
       public         heap    postgres    false            �            1259    17039    auth_user_groups_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.auth_user_groups_id_seq;
       public          postgres    false    233            _           0    0    auth_user_groups_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;
          public          postgres    false    232            �            1259    17030    auth_user_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.auth_user_id_seq;
       public          postgres    false    231            `           0    0    auth_user_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;
          public          postgres    false    230            �            1259    17047    auth_user_user_permissions    TABLE     �   CREATE TABLE public.auth_user_user_permissions (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);
 .   DROP TABLE public.auth_user_user_permissions;
       public         heap    postgres    false            �            1259    17046 !   auth_user_user_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public.auth_user_user_permissions_id_seq;
       public          postgres    false    235            a           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE OWNED BY     g   ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;
          public          postgres    false    234            �            1259    17286    communication_faq    TABLE     ]   CREATE TABLE public.communication_faq (
    id bigint NOT NULL,
    _faq boolean NOT NULL
);
 %   DROP TABLE public.communication_faq;
       public         heap    postgres    false            �            1259    17285    communication_faq_id_seq    SEQUENCE     �   CREATE SEQUENCE public.communication_faq_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.communication_faq_id_seq;
       public          postgres    false    253            b           0    0    communication_faq_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.communication_faq_id_seq OWNED BY public.communication_faq.id;
          public          postgres    false    252                       1259    17331    communication_forum    TABLE     �   CREATE TABLE public.communication_forum (
    id bigint NOT NULL,
    _forum boolean NOT NULL,
    name character varying(30) NOT NULL
);
 '   DROP TABLE public.communication_forum;
       public         heap    postgres    false                       1259    17330    communication_forum_id_seq    SEQUENCE     �   CREATE SEQUENCE public.communication_forum_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.communication_forum_id_seq;
       public          postgres    false    259            c           0    0    communication_forum_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.communication_forum_id_seq OWNED BY public.communication_forum.id;
          public          postgres    false    258                       1259    17316    communication_notification    TABLE       CREATE TABLE public.communication_notification (
    id bigint NOT NULL,
    header character varying(100) NOT NULL,
    link character varying(200) NOT NULL,
    is_flagged boolean NOT NULL,
    date timestamp with time zone,
    user_id bigint NOT NULL
);
 .   DROP TABLE public.communication_notification;
       public         heap    postgres    false                        1259    17315 !   communication_notification_id_seq    SEQUENCE     �   CREATE SEQUENCE public.communication_notification_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public.communication_notification_id_seq;
       public          postgres    false    257            d           0    0 !   communication_notification_id_seq    SEQUENCE OWNED BY     g   ALTER SEQUENCE public.communication_notification_id_seq OWNED BY public.communication_notification.id;
          public          postgres    false    256                       1259    17340    communication_post    TABLE     �   CREATE TABLE public.communication_post (
    id bigint NOT NULL,
    date timestamp with time zone NOT NULL,
    topic character varying(50) NOT NULL,
    text text NOT NULL,
    forum_id bigint NOT NULL,
    user_id bigint NOT NULL
);
 &   DROP TABLE public.communication_post;
       public         heap    postgres    false                       1259    17339    communication_post_id_seq    SEQUENCE     �   CREATE SEQUENCE public.communication_post_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.communication_post_id_seq;
       public          postgres    false    261            e           0    0    communication_post_id_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public.communication_post_id_seq OWNED BY public.communication_post.id;
          public          postgres    false    260            �            1259    17295    communication_question    TABLE     �   CREATE TABLE public.communication_question (
    id bigint NOT NULL,
    question text NOT NULL,
    answer text NOT NULL,
    faq_id bigint NOT NULL,
    user_id bigint NOT NULL
);
 *   DROP TABLE public.communication_question;
       public         heap    postgres    false            �            1259    17294    communication_question_id_seq    SEQUENCE     �   CREATE SEQUENCE public.communication_question_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.communication_question_id_seq;
       public          postgres    false    255            f           0    0    communication_question_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.communication_question_id_seq OWNED BY public.communication_question.id;
          public          postgres    false    254                       1259    17349    communication_response    TABLE     �   CREATE TABLE public.communication_response (
    id bigint NOT NULL,
    date timestamp with time zone NOT NULL,
    text text NOT NULL,
    post_id bigint NOT NULL,
    user_id bigint NOT NULL
);
 *   DROP TABLE public.communication_response;
       public         heap    postgres    false                       1259    17348    communication_response_id_seq    SEQUENCE     �   CREATE SEQUENCE public.communication_response_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.communication_response_id_seq;
       public          postgres    false    263            g           0    0    communication_response_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.communication_response_id_seq OWNED BY public.communication_response.id;
          public          postgres    false    262            
           1259    17393    courses_bilkentcourse    TABLE     z  CREATE TABLE public.courses_bilkentcourse (
    id bigint NOT NULL,
    course_name character varying(100) NOT NULL,
    course_code character varying(20) NOT NULL,
    course_credit double precision NOT NULL,
    course_type character varying(30) NOT NULL,
    elective_group_name character varying(100) NOT NULL,
    course_coordinator_name character varying(100) NOT NULL
);
 )   DROP TABLE public.courses_bilkentcourse;
       public         heap    postgres    false            	           1259    17392    courses_bilkentcourse_id_seq    SEQUENCE     �   CREATE SEQUENCE public.courses_bilkentcourse_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 3   DROP SEQUENCE public.courses_bilkentcourse_id_seq;
       public          postgres    false    266            h           0    0    courses_bilkentcourse_id_seq    SEQUENCE OWNED BY     ]   ALTER SEQUENCE public.courses_bilkentcourse_id_seq OWNED BY public.courses_bilkentcourse.id;
          public          postgres    false    265            �            1259    16953    courses_course    TABLE     �  CREATE TABLE public.courses_course (
    id bigint NOT NULL,
    course_name character varying(100) NOT NULL,
    course_credit double precision NOT NULL,
    approved boolean NOT NULL,
    bilkent_equivalent_id bigint,
    is_merged boolean NOT NULL,
    merged_course_id bigint,
    university_id bigint,
    is_rejected boolean NOT NULL,
    code character varying(20) NOT NULL,
    submitted boolean NOT NULL
);
 "   DROP TABLE public.courses_course;
       public         heap    postgres    false            �            1259    16952    courses_course_id_seq    SEQUENCE     ~   CREATE SEQUENCE public.courses_course_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.courses_course_id_seq;
       public          postgres    false    217            i           0    0    courses_course_id_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public.courses_course_id_seq OWNED BY public.courses_course.id;
          public          postgres    false    216            �            1259    17218    courses_document    TABLE     h  CREATE TABLE public.courses_document (
    id bigint NOT NULL,
    document_name character varying(50) NOT NULL,
    document character varying(100) NOT NULL,
    date timestamp with time zone NOT NULL,
    is_signed boolean NOT NULL,
    document_type character varying(20) NOT NULL,
    user_id bigint NOT NULL,
    is_signed_coordinator boolean NOT NULL
);
 $   DROP TABLE public.courses_document;
       public         heap    postgres    false            �            1259    17217    courses_document_id_seq    SEQUENCE     �   CREATE SEQUENCE public.courses_document_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.courses_document_id_seq;
       public          postgres    false    249            j           0    0    courses_document_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.courses_document_id_seq OWNED BY public.courses_document.id;
          public          postgres    false    248            �            1259    16973    courses_mergedcourse    TABLE     �   CREATE TABLE public.courses_mergedcourse (
    id bigint NOT NULL,
    bilkent_equivalent_id bigint,
    approved boolean NOT NULL,
    is_rejected boolean NOT NULL,
    submitted boolean NOT NULL
);
 (   DROP TABLE public.courses_mergedcourse;
       public         heap    postgres    false            �            1259    16972    courses_mergedcourse_id_seq    SEQUENCE     �   CREATE SEQUENCE public.courses_mergedcourse_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.courses_mergedcourse_id_seq;
       public          postgres    false    221            k           0    0    courses_mergedcourse_id_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public.courses_mergedcourse_id_seq OWNED BY public.courses_mergedcourse.id;
          public          postgres    false    220            �            1259    16960    courses_university    TABLE     �  CREATE TABLE public.courses_university (
    id bigint NOT NULL,
    university_name character varying(100) NOT NULL,
    country character varying(50) NOT NULL,
    lowest_grade character varying(20) NOT NULL,
    highest_grade character varying(20) NOT NULL,
    passing_grade character varying(20) NOT NULL,
    inverted_scale boolean NOT NULL,
    department character varying(200) NOT NULL
);
 &   DROP TABLE public.courses_university;
       public         heap    postgres    false            �            1259    16959    courses_university_id_seq    SEQUENCE     �   CREATE SEQUENCE public.courses_university_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.courses_university_id_seq;
       public          postgres    false    219            l           0    0    courses_university_id_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public.courses_university_id_seq OWNED BY public.courses_university.id;
          public          postgres    false    218            �            1259    17241    django_admin_log    TABLE     �  CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);
 $   DROP TABLE public.django_admin_log;
       public         heap    postgres    false            �            1259    17240    django_admin_log_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.django_admin_log_id_seq;
       public          postgres    false    251            m           0    0    django_admin_log_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;
          public          postgres    false    250            �            1259    16999    django_content_type    TABLE     �   CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);
 '   DROP TABLE public.django_content_type;
       public         heap    postgres    false            �            1259    16998    django_content_type_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.django_content_type_id_seq;
       public          postgres    false    223            n           0    0    django_content_type_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;
          public          postgres    false    222            �            1259    16944    django_migrations    TABLE     �   CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);
 %   DROP TABLE public.django_migrations;
       public         heap    postgres    false            �            1259    16943    django_migrations_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.django_migrations_id_seq;
       public          postgres    false    215            o           0    0    django_migrations_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;
          public          postgres    false    214                       1259    17382    django_session    TABLE     �   CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);
 "   DROP TABLE public.django_session;
       public         heap    postgres    false            �           2604    17141    accounts_boardmember id    DEFAULT     �   ALTER TABLE ONLY public.accounts_boardmember ALTER COLUMN id SET DEFAULT nextval('public.accounts_boardmember_id_seq'::regclass);
 F   ALTER TABLE public.accounts_boardmember ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    243    242    243            �           2604    17132    accounts_coordinator id    DEFAULT     �   ALTER TABLE ONLY public.accounts_coordinator ALTER COLUMN id SET DEFAULT nextval('public.accounts_coordinator_id_seq'::regclass);
 F   ALTER TABLE public.accounts_coordinator ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    240    241    241            �           2604    17109    accounts_erasmususer id    DEFAULT     �   ALTER TABLE ONLY public.accounts_erasmususer ALTER COLUMN id SET DEFAULT nextval('public.accounts_erasmususer_id_seq'::regclass);
 F   ALTER TABLE public.accounts_erasmususer ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    237    236    237            �           2604    17123    accounts_student id    DEFAULT     z   ALTER TABLE ONLY public.accounts_student ALTER COLUMN id SET DEFAULT nextval('public.accounts_student_id_seq'::regclass);
 B   ALTER TABLE public.accounts_student ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    238    239    239            �           2604    17184    accounts_todo id    DEFAULT     t   ALTER TABLE ONLY public.accounts_todo ALTER COLUMN id SET DEFAULT nextval('public.accounts_todo_id_seq'::regclass);
 ?   ALTER TABLE public.accounts_todo ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    247    246    247            �           2604    17165    accounts_usercourse id    DEFAULT     �   ALTER TABLE ONLY public.accounts_usercourse ALTER COLUMN id SET DEFAULT nextval('public.accounts_usercourse_id_seq'::regclass);
 E   ALTER TABLE public.accounts_usercourse ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    245    244    245            �           2604    17018    auth_group id    DEFAULT     n   ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);
 <   ALTER TABLE public.auth_group ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    226    227    227            �           2604    17027    auth_group_permissions id    DEFAULT     �   ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);
 H   ALTER TABLE public.auth_group_permissions ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    228    229    229            �           2604    17011    auth_permission id    DEFAULT     x   ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);
 A   ALTER TABLE public.auth_permission ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    224    225    225            �           2604    17034    auth_user id    DEFAULT     l   ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);
 ;   ALTER TABLE public.auth_user ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    231    230    231            �           2604    17043    auth_user_groups id    DEFAULT     z   ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);
 B   ALTER TABLE public.auth_user_groups ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    232    233    233            �           2604    17050    auth_user_user_permissions id    DEFAULT     �   ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);
 L   ALTER TABLE public.auth_user_user_permissions ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    235    234    235            �           2604    17289    communication_faq id    DEFAULT     |   ALTER TABLE ONLY public.communication_faq ALTER COLUMN id SET DEFAULT nextval('public.communication_faq_id_seq'::regclass);
 C   ALTER TABLE public.communication_faq ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    252    253    253            �           2604    17334    communication_forum id    DEFAULT     �   ALTER TABLE ONLY public.communication_forum ALTER COLUMN id SET DEFAULT nextval('public.communication_forum_id_seq'::regclass);
 E   ALTER TABLE public.communication_forum ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    258    259    259            �           2604    17319    communication_notification id    DEFAULT     �   ALTER TABLE ONLY public.communication_notification ALTER COLUMN id SET DEFAULT nextval('public.communication_notification_id_seq'::regclass);
 L   ALTER TABLE public.communication_notification ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    257    256    257            �           2604    17343    communication_post id    DEFAULT     ~   ALTER TABLE ONLY public.communication_post ALTER COLUMN id SET DEFAULT nextval('public.communication_post_id_seq'::regclass);
 D   ALTER TABLE public.communication_post ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    261    260    261            �           2604    17298    communication_question id    DEFAULT     �   ALTER TABLE ONLY public.communication_question ALTER COLUMN id SET DEFAULT nextval('public.communication_question_id_seq'::regclass);
 H   ALTER TABLE public.communication_question ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    255    254    255            �           2604    17352    communication_response id    DEFAULT     �   ALTER TABLE ONLY public.communication_response ALTER COLUMN id SET DEFAULT nextval('public.communication_response_id_seq'::regclass);
 H   ALTER TABLE public.communication_response ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    263    262    263            �           2604    17396    courses_bilkentcourse id    DEFAULT     �   ALTER TABLE ONLY public.courses_bilkentcourse ALTER COLUMN id SET DEFAULT nextval('public.courses_bilkentcourse_id_seq'::regclass);
 G   ALTER TABLE public.courses_bilkentcourse ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    265    266    266            �           2604    16956    courses_course id    DEFAULT     v   ALTER TABLE ONLY public.courses_course ALTER COLUMN id SET DEFAULT nextval('public.courses_course_id_seq'::regclass);
 @   ALTER TABLE public.courses_course ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    216    217    217            �           2604    17221    courses_document id    DEFAULT     z   ALTER TABLE ONLY public.courses_document ALTER COLUMN id SET DEFAULT nextval('public.courses_document_id_seq'::regclass);
 B   ALTER TABLE public.courses_document ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    248    249    249            �           2604    16976    courses_mergedcourse id    DEFAULT     �   ALTER TABLE ONLY public.courses_mergedcourse ALTER COLUMN id SET DEFAULT nextval('public.courses_mergedcourse_id_seq'::regclass);
 F   ALTER TABLE public.courses_mergedcourse ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    220    221    221            �           2604    16963    courses_university id    DEFAULT     ~   ALTER TABLE ONLY public.courses_university ALTER COLUMN id SET DEFAULT nextval('public.courses_university_id_seq'::regclass);
 D   ALTER TABLE public.courses_university ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    219    218    219            �           2604    17244    django_admin_log id    DEFAULT     z   ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);
 B   ALTER TABLE public.django_admin_log ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    250    251    251            �           2604    17002    django_content_type id    DEFAULT     �   ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);
 E   ALTER TABLE public.django_content_type ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    222    223    223            �           2604    16947    django_migrations id    DEFAULT     |   ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);
 C   ALTER TABLE public.django_migrations ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    214    215    215            8          0    17138    accounts_boardmember 
   TABLE DATA           ;   COPY public.accounts_boardmember (id, user_id) FROM stdin;
    public          postgres    false    243   �f      6          0    17129    accounts_coordinator 
   TABLE DATA           ;   COPY public.accounts_coordinator (id, user_id) FROM stdin;
    public          postgres    false    241   �f      2          0    17106    accounts_erasmususer 
   TABLE DATA           g   COPY public.accounts_erasmususer (id, email, bilkent_id, phone, user_id, name, department) FROM stdin;
    public          postgres    false    237   �f      4          0    17120    accounts_student 
   TABLE DATA           �   COPY public.accounts_student (id, gpa, score, status, is_erasmus_done, user_id, coordinator_id, academic_year, semester, university_id, email_visibility, mobility_visiblity, phone_visibility, status_visibility, final_list_approved) FROM stdin;
    public          postgres    false    239   ag      <          0    17181    accounts_todo 
   TABLE DATA           g   COPY public.accounts_todo (id, header, body, link, is_flagged, is_done, due_date, user_id) FROM stdin;
    public          postgres    false    247   �g      :          0    17162    accounts_usercourse 
   TABLE DATA           W   COPY public.accounts_usercourse (id, grade, course_id, user_id, submitted) FROM stdin;
    public          postgres    false    245   Mh      (          0    17015 
   auth_group 
   TABLE DATA           .   COPY public.auth_group (id, name) FROM stdin;
    public          postgres    false    227   ~h      *          0    17024    auth_group_permissions 
   TABLE DATA           M   COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
    public          postgres    false    229   �h      &          0    17008    auth_permission 
   TABLE DATA           N   COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
    public          postgres    false    225   �h      ,          0    17031 	   auth_user 
   TABLE DATA           �   COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
    public          postgres    false    231   7l      .          0    17040    auth_user_groups 
   TABLE DATA           A   COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
    public          postgres    false    233   �m      0          0    17047    auth_user_user_permissions 
   TABLE DATA           P   COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
    public          postgres    false    235   �m      B          0    17286    communication_faq 
   TABLE DATA           5   COPY public.communication_faq (id, _faq) FROM stdin;
    public          postgres    false    253   gp      H          0    17331    communication_forum 
   TABLE DATA           ?   COPY public.communication_forum (id, _forum, name) FROM stdin;
    public          postgres    false    259   �p      F          0    17316    communication_notification 
   TABLE DATA           a   COPY public.communication_notification (id, header, link, is_flagged, date, user_id) FROM stdin;
    public          postgres    false    257   �p      J          0    17340    communication_post 
   TABLE DATA           V   COPY public.communication_post (id, date, topic, text, forum_id, user_id) FROM stdin;
    public          postgres    false    261   �p      D          0    17295    communication_question 
   TABLE DATA           W   COPY public.communication_question (id, question, answer, faq_id, user_id) FROM stdin;
    public          postgres    false    255   1q      L          0    17349    communication_response 
   TABLE DATA           R   COPY public.communication_response (id, date, text, post_id, user_id) FROM stdin;
    public          postgres    false    263   Nq      O          0    17393    courses_bilkentcourse 
   TABLE DATA           �   COPY public.courses_bilkentcourse (id, course_name, course_code, course_credit, course_type, elective_group_name, course_coordinator_name) FROM stdin;
    public          postgres    false    266   kq                0    16953    courses_course 
   TABLE DATA           �   COPY public.courses_course (id, course_name, course_credit, approved, bilkent_equivalent_id, is_merged, merged_course_id, university_id, is_rejected, code, submitted) FROM stdin;
    public          postgres    false    217   �q      >          0    17218    courses_document 
   TABLE DATA           �   COPY public.courses_document (id, document_name, document, date, is_signed, document_type, user_id, is_signed_coordinator) FROM stdin;
    public          postgres    false    249   r      "          0    16973    courses_mergedcourse 
   TABLE DATA           k   COPY public.courses_mergedcourse (id, bilkent_equivalent_id, approved, is_rejected, submitted) FROM stdin;
    public          postgres    false    221   �r                 0    16960    courses_university 
   TABLE DATA           �   COPY public.courses_university (id, university_name, country, lowest_grade, highest_grade, passing_grade, inverted_scale, department) FROM stdin;
    public          postgres    false    219   s      @          0    17241    django_admin_log 
   TABLE DATA           �   COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
    public          postgres    false    251   Ts      $          0    16999    django_content_type 
   TABLE DATA           C   COPY public.django_content_type (id, app_label, model) FROM stdin;
    public          postgres    false    223   �t                0    16944    django_migrations 
   TABLE DATA           C   COPY public.django_migrations (id, app, name, applied) FROM stdin;
    public          postgres    false    215   �u      M          0    17382    django_session 
   TABLE DATA           P   COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
    public          postgres    false    264   i{      p           0    0    accounts_boardmember_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.accounts_boardmember_id_seq', 1, false);
          public          postgres    false    242            q           0    0    accounts_coordinator_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.accounts_coordinator_id_seq', 1, true);
          public          postgres    false    240            r           0    0    accounts_erasmususer_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.accounts_erasmususer_id_seq', 2, true);
          public          postgres    false    236            s           0    0    accounts_student_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.accounts_student_id_seq', 1, true);
          public          postgres    false    238            t           0    0    accounts_todo_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.accounts_todo_id_seq', 3, true);
          public          postgres    false    246            u           0    0    accounts_usercourse_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.accounts_usercourse_id_seq', 3, true);
          public          postgres    false    244            v           0    0    auth_group_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);
          public          postgres    false    226            w           0    0    auth_group_permissions_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);
          public          postgres    false    228            x           0    0    auth_permission_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.auth_permission_id_seq', 92, true);
          public          postgres    false    224            y           0    0    auth_user_groups_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);
          public          postgres    false    232            z           0    0    auth_user_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.auth_user_id_seq', 3, true);
          public          postgres    false    230            {           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE SET     Q   SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 184, true);
          public          postgres    false    234            |           0    0    communication_faq_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.communication_faq_id_seq', 1, false);
          public          postgres    false    252            }           0    0    communication_forum_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.communication_forum_id_seq', 1, true);
          public          postgres    false    258            ~           0    0 !   communication_notification_id_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public.communication_notification_id_seq', 1, false);
          public          postgres    false    256                       0    0    communication_post_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.communication_post_id_seq', 2, true);
          public          postgres    false    260            �           0    0    communication_question_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.communication_question_id_seq', 1, false);
          public          postgres    false    254            �           0    0    communication_response_id_seq    SEQUENCE SET     K   SELECT pg_catalog.setval('public.communication_response_id_seq', 5, true);
          public          postgres    false    262            �           0    0    courses_bilkentcourse_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.courses_bilkentcourse_id_seq', 1, true);
          public          postgres    false    265            �           0    0    courses_course_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.courses_course_id_seq', 3, true);
          public          postgres    false    216            �           0    0    courses_document_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.courses_document_id_seq', 5, true);
          public          postgres    false    248            �           0    0    courses_mergedcourse_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.courses_mergedcourse_id_seq', 1, true);
          public          postgres    false    220            �           0    0    courses_university_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.courses_university_id_seq', 1, true);
          public          postgres    false    218            �           0    0    django_admin_log_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.django_admin_log_id_seq', 13, true);
          public          postgres    false    250            �           0    0    django_content_type_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.django_content_type_id_seq', 23, true);
          public          postgres    false    222            �           0    0    django_migrations_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.django_migrations_id_seq', 65, true);
          public          postgres    false    214            A           2606    17143 .   accounts_boardmember accounts_boardmember_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public.accounts_boardmember
    ADD CONSTRAINT accounts_boardmember_pkey PRIMARY KEY (id);
 X   ALTER TABLE ONLY public.accounts_boardmember DROP CONSTRAINT accounts_boardmember_pkey;
       public            postgres    false    243            C           2606    17145 5   accounts_boardmember accounts_boardmember_user_id_key 
   CONSTRAINT     s   ALTER TABLE ONLY public.accounts_boardmember
    ADD CONSTRAINT accounts_boardmember_user_id_key UNIQUE (user_id);
 _   ALTER TABLE ONLY public.accounts_boardmember DROP CONSTRAINT accounts_boardmember_user_id_key;
       public            postgres    false    243            =           2606    17134 .   accounts_coordinator accounts_coordinator_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public.accounts_coordinator
    ADD CONSTRAINT accounts_coordinator_pkey PRIMARY KEY (id);
 X   ALTER TABLE ONLY public.accounts_coordinator DROP CONSTRAINT accounts_coordinator_pkey;
       public            postgres    false    241            ?           2606    17136 5   accounts_coordinator accounts_coordinator_user_id_key 
   CONSTRAINT     s   ALTER TABLE ONLY public.accounts_coordinator
    ADD CONSTRAINT accounts_coordinator_user_id_key UNIQUE (user_id);
 _   ALTER TABLE ONLY public.accounts_coordinator DROP CONSTRAINT accounts_coordinator_user_id_key;
       public            postgres    false    241            3           2606    17111 .   accounts_erasmususer accounts_erasmususer_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public.accounts_erasmususer
    ADD CONSTRAINT accounts_erasmususer_pkey PRIMARY KEY (id);
 X   ALTER TABLE ONLY public.accounts_erasmususer DROP CONSTRAINT accounts_erasmususer_pkey;
       public            postgres    false    237            5           2606    17113 5   accounts_erasmususer accounts_erasmususer_user_id_key 
   CONSTRAINT     s   ALTER TABLE ONLY public.accounts_erasmususer
    ADD CONSTRAINT accounts_erasmususer_user_id_key UNIQUE (user_id);
 _   ALTER TABLE ONLY public.accounts_erasmususer DROP CONSTRAINT accounts_erasmususer_user_id_key;
       public            postgres    false    237            8           2606    17125 &   accounts_student accounts_student_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.accounts_student
    ADD CONSTRAINT accounts_student_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.accounts_student DROP CONSTRAINT accounts_student_pkey;
       public            postgres    false    239            ;           2606    17127 -   accounts_student accounts_student_user_id_key 
   CONSTRAINT     k   ALTER TABLE ONLY public.accounts_student
    ADD CONSTRAINT accounts_student_user_id_key UNIQUE (user_id);
 W   ALTER TABLE ONLY public.accounts_student DROP CONSTRAINT accounts_student_user_id_key;
       public            postgres    false    239            I           2606    17188     accounts_todo accounts_todo_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public.accounts_todo
    ADD CONSTRAINT accounts_todo_pkey PRIMARY KEY (id);
 J   ALTER TABLE ONLY public.accounts_todo DROP CONSTRAINT accounts_todo_pkey;
       public            postgres    false    247            F           2606    17167 ,   accounts_usercourse accounts_usercourse_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.accounts_usercourse
    ADD CONSTRAINT accounts_usercourse_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.accounts_usercourse DROP CONSTRAINT accounts_usercourse_pkey;
       public            postgres    false    245                       2606    17268    auth_group auth_group_name_key 
   CONSTRAINT     Y   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);
 H   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_name_key;
       public            postgres    false    227                       2606    17063 R   auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);
 |   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq;
       public            postgres    false    229    229                        2606    17029 2   auth_group_permissions auth_group_permissions_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_pkey;
       public            postgres    false    229                       2606    17020    auth_group auth_group_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_pkey;
       public            postgres    false    227                       2606    17054 F   auth_permission auth_permission_content_type_id_codename_01ab375a_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);
 p   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq;
       public            postgres    false    225    225                       2606    17013 $   auth_permission auth_permission_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_pkey;
       public            postgres    false    225            (           2606    17045 &   auth_user_groups auth_user_groups_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_pkey;
       public            postgres    false    233            +           2606    17078 @   auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);
 j   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq;
       public            postgres    false    233    233            "           2606    17036    auth_user auth_user_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_pkey;
       public            postgres    false    231            .           2606    17052 :   auth_user_user_permissions auth_user_user_permissions_pkey 
   CONSTRAINT     x   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);
 d   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_pkey;
       public            postgres    false    235            1           2606    17092 Y   auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);
 �   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq;
       public            postgres    false    235    235            %           2606    17263     auth_user auth_user_username_key 
   CONSTRAINT     _   ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);
 J   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_username_key;
       public            postgres    false    231            S           2606    17293 ,   communication_faq communication_faq__faq_key 
   CONSTRAINT     g   ALTER TABLE ONLY public.communication_faq
    ADD CONSTRAINT communication_faq__faq_key UNIQUE (_faq);
 V   ALTER TABLE ONLY public.communication_faq DROP CONSTRAINT communication_faq__faq_key;
       public            postgres    false    253            U           2606    17291 (   communication_faq communication_faq_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.communication_faq
    ADD CONSTRAINT communication_faq_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.communication_faq DROP CONSTRAINT communication_faq_pkey;
       public            postgres    false    253            ^           2606    17338 2   communication_forum communication_forum__forum_key 
   CONSTRAINT     o   ALTER TABLE ONLY public.communication_forum
    ADD CONSTRAINT communication_forum__forum_key UNIQUE (_forum);
 \   ALTER TABLE ONLY public.communication_forum DROP CONSTRAINT communication_forum__forum_key;
       public            postgres    false    259            `           2606    17336 ,   communication_forum communication_forum_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.communication_forum
    ADD CONSTRAINT communication_forum_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.communication_forum DROP CONSTRAINT communication_forum_pkey;
       public            postgres    false    259            [           2606    17323 :   communication_notification communication_notification_pkey 
   CONSTRAINT     x   ALTER TABLE ONLY public.communication_notification
    ADD CONSTRAINT communication_notification_pkey PRIMARY KEY (id);
 d   ALTER TABLE ONLY public.communication_notification DROP CONSTRAINT communication_notification_pkey;
       public            postgres    false    257            c           2606    17347 *   communication_post communication_post_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY public.communication_post
    ADD CONSTRAINT communication_post_pkey PRIMARY KEY (id);
 T   ALTER TABLE ONLY public.communication_post DROP CONSTRAINT communication_post_pkey;
       public            postgres    false    261            X           2606    17302 2   communication_question communication_question_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.communication_question
    ADD CONSTRAINT communication_question_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.communication_question DROP CONSTRAINT communication_question_pkey;
       public            postgres    false    255            f           2606    17356 2   communication_response communication_response_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.communication_response
    ADD CONSTRAINT communication_response_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.communication_response DROP CONSTRAINT communication_response_pkey;
       public            postgres    false    263            n           2606    17398 0   courses_bilkentcourse courses_bilkentcourse_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public.courses_bilkentcourse
    ADD CONSTRAINT courses_bilkentcourse_pkey PRIMARY KEY (id);
 Z   ALTER TABLE ONLY public.courses_bilkentcourse DROP CONSTRAINT courses_bilkentcourse_pkey;
       public            postgres    false    266                       2606    16958 "   courses_course courses_course_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public.courses_course
    ADD CONSTRAINT courses_course_pkey PRIMARY KEY (id);
 L   ALTER TABLE ONLY public.courses_course DROP CONSTRAINT courses_course_pkey;
       public            postgres    false    217            L           2606    17223 &   courses_document courses_document_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.courses_document
    ADD CONSTRAINT courses_document_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.courses_document DROP CONSTRAINT courses_document_pkey;
       public            postgres    false    249                       2606    16978 .   courses_mergedcourse courses_mergedcourse_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public.courses_mergedcourse
    ADD CONSTRAINT courses_mergedcourse_pkey PRIMARY KEY (id);
 X   ALTER TABLE ONLY public.courses_mergedcourse DROP CONSTRAINT courses_mergedcourse_pkey;
       public            postgres    false    221            	           2606    16965 *   courses_university courses_university_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY public.courses_university
    ADD CONSTRAINT courses_university_pkey PRIMARY KEY (id);
 T   ALTER TABLE ONLY public.courses_university DROP CONSTRAINT courses_university_pkey;
       public            postgres    false    219            P           2606    17249 &   django_admin_log django_admin_log_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_pkey;
       public            postgres    false    251                       2606    17006 E   django_content_type django_content_type_app_label_model_76bd3d3b_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);
 o   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq;
       public            postgres    false    223    223                       2606    17004 ,   django_content_type django_content_type_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_pkey;
       public            postgres    false    223                       2606    16951 (   django_migrations django_migrations_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.django_migrations DROP CONSTRAINT django_migrations_pkey;
       public            postgres    false    215            k           2606    17388 "   django_session django_session_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);
 L   ALTER TABLE ONLY public.django_session DROP CONSTRAINT django_session_pkey;
       public            postgres    false    264            6           1259    17216 (   accounts_student_coordinator_id_fca0fe7e    INDEX     o   CREATE INDEX accounts_student_coordinator_id_fca0fe7e ON public.accounts_student USING btree (coordinator_id);
 <   DROP INDEX public.accounts_student_coordinator_id_fca0fe7e;
       public            postgres    false    239            9           1259    17239 '   accounts_student_university_id_3d025979    INDEX     m   CREATE INDEX accounts_student_university_id_3d025979 ON public.accounts_student USING btree (university_id);
 ;   DROP INDEX public.accounts_student_university_id_3d025979;
       public            postgres    false    239            J           1259    17202    accounts_todo_user_id_e49e7c03    INDEX     [   CREATE INDEX accounts_todo_user_id_e49e7c03 ON public.accounts_todo USING btree (user_id);
 2   DROP INDEX public.accounts_todo_user_id_e49e7c03;
       public            postgres    false    247            D           1259    17178 &   accounts_usercourse_course_id_aa6ceb08    INDEX     k   CREATE INDEX accounts_usercourse_course_id_aa6ceb08 ON public.accounts_usercourse USING btree (course_id);
 :   DROP INDEX public.accounts_usercourse_course_id_aa6ceb08;
       public            postgres    false    245            G           1259    17179 $   accounts_usercourse_user_id_1e7fd3bb    INDEX     g   CREATE INDEX accounts_usercourse_user_id_1e7fd3bb ON public.accounts_usercourse USING btree (user_id);
 8   DROP INDEX public.accounts_usercourse_user_id_1e7fd3bb;
       public            postgres    false    245                       1259    17269    auth_group_name_a6ea08ec_like    INDEX     h   CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);
 1   DROP INDEX public.auth_group_name_a6ea08ec_like;
       public            postgres    false    227                       1259    17074 (   auth_group_permissions_group_id_b120cbf9    INDEX     o   CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);
 <   DROP INDEX public.auth_group_permissions_group_id_b120cbf9;
       public            postgres    false    229                       1259    17075 -   auth_group_permissions_permission_id_84c5c92e    INDEX     y   CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);
 A   DROP INDEX public.auth_group_permissions_permission_id_84c5c92e;
       public            postgres    false    229                       1259    17060 (   auth_permission_content_type_id_2f476e4b    INDEX     o   CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);
 <   DROP INDEX public.auth_permission_content_type_id_2f476e4b;
       public            postgres    false    225            &           1259    17090 "   auth_user_groups_group_id_97559544    INDEX     c   CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);
 6   DROP INDEX public.auth_user_groups_group_id_97559544;
       public            postgres    false    233            )           1259    17089 !   auth_user_groups_user_id_6a12ed8b    INDEX     a   CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);
 5   DROP INDEX public.auth_user_groups_user_id_6a12ed8b;
       public            postgres    false    233            ,           1259    17104 1   auth_user_user_permissions_permission_id_1fbb5f2c    INDEX     �   CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);
 E   DROP INDEX public.auth_user_user_permissions_permission_id_1fbb5f2c;
       public            postgres    false    235            /           1259    17103 +   auth_user_user_permissions_user_id_a95ead1b    INDEX     u   CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);
 ?   DROP INDEX public.auth_user_user_permissions_user_id_a95ead1b;
       public            postgres    false    235            #           1259    17264     auth_user_username_6821ab7c_like    INDEX     n   CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);
 4   DROP INDEX public.auth_user_username_6821ab7c_like;
       public            postgres    false    231            \           1259    17329 +   communication_notification_user_id_6611ccd5    INDEX     u   CREATE INDEX communication_notification_user_id_6611ccd5 ON public.communication_notification USING btree (user_id);
 ?   DROP INDEX public.communication_notification_user_id_6611ccd5;
       public            postgres    false    257            a           1259    17367 $   communication_post_forum_id_216369dc    INDEX     g   CREATE INDEX communication_post_forum_id_216369dc ON public.communication_post USING btree (forum_id);
 8   DROP INDEX public.communication_post_forum_id_216369dc;
       public            postgres    false    261            d           1259    17368 #   communication_post_user_id_22b39414    INDEX     e   CREATE INDEX communication_post_user_id_22b39414 ON public.communication_post USING btree (user_id);
 7   DROP INDEX public.communication_post_user_id_22b39414;
       public            postgres    false    261            V           1259    17313 &   communication_question_faq_id_4871d988    INDEX     k   CREATE INDEX communication_question_faq_id_4871d988 ON public.communication_question USING btree (faq_id);
 :   DROP INDEX public.communication_question_faq_id_4871d988;
       public            postgres    false    255            Y           1259    17314 '   communication_question_user_id_30f264db    INDEX     m   CREATE INDEX communication_question_user_id_30f264db ON public.communication_question USING btree (user_id);
 ;   DROP INDEX public.communication_question_user_id_30f264db;
       public            postgres    false    255            g           1259    17379 '   communication_response_post_id_b8ed270b    INDEX     m   CREATE INDEX communication_response_post_id_b8ed270b ON public.communication_response USING btree (post_id);
 ;   DROP INDEX public.communication_response_post_id_b8ed270b;
       public            postgres    false    263            h           1259    17380 '   communication_response_user_id_e3b25a8f    INDEX     m   CREATE INDEX communication_response_user_id_e3b25a8f ON public.communication_response USING btree (user_id);
 ;   DROP INDEX public.communication_response_user_id_e3b25a8f;
       public            postgres    false    263                       1259    16989 -   courses_course_bilkent_equivalent_id_d03581e2    INDEX     y   CREATE INDEX courses_course_bilkent_equivalent_id_d03581e2 ON public.courses_course USING btree (bilkent_equivalent_id);
 A   DROP INDEX public.courses_course_bilkent_equivalent_id_d03581e2;
       public            postgres    false    217                       1259    16996 (   courses_course_merged_course_id_3eda05f5    INDEX     o   CREATE INDEX courses_course_merged_course_id_3eda05f5 ON public.courses_course USING btree (merged_course_id);
 <   DROP INDEX public.courses_course_merged_course_id_3eda05f5;
       public            postgres    false    217                       1259    16997 %   courses_course_university_id_65d105dd    INDEX     i   CREATE INDEX courses_course_university_id_65d105dd ON public.courses_course USING btree (university_id);
 9   DROP INDEX public.courses_course_university_id_65d105dd;
       public            postgres    false    217            M           1259    17229 !   courses_document_user_id_0942113d    INDEX     a   CREATE INDEX courses_document_user_id_0942113d ON public.courses_document USING btree (user_id);
 5   DROP INDEX public.courses_document_user_id_0942113d;
       public            postgres    false    249            
           1259    16995 3   courses_mergedcourse_bilkent_equivalent_id_06d38cc6    INDEX     �   CREATE INDEX courses_mergedcourse_bilkent_equivalent_id_06d38cc6 ON public.courses_mergedcourse USING btree (bilkent_equivalent_id);
 G   DROP INDEX public.courses_mergedcourse_bilkent_equivalent_id_06d38cc6;
       public            postgres    false    221            N           1259    17260 )   django_admin_log_content_type_id_c4bce8eb    INDEX     q   CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);
 =   DROP INDEX public.django_admin_log_content_type_id_c4bce8eb;
       public            postgres    false    251            Q           1259    17261 !   django_admin_log_user_id_c564eba6    INDEX     a   CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);
 5   DROP INDEX public.django_admin_log_user_id_c564eba6;
       public            postgres    false    251            i           1259    17390 #   django_session_expire_date_a5c62663    INDEX     e   CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);
 7   DROP INDEX public.django_session_expire_date_a5c62663;
       public            postgres    false    264            l           1259    17389 (   django_session_session_key_c0390e0f_like    INDEX     ~   CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);
 <   DROP INDEX public.django_session_session_key_c0390e0f_like;
       public            postgres    false    264                       2606    17156 G   accounts_boardmember accounts_boardmember_user_id_f214d4c8_fk_accounts_    FK CONSTRAINT     �   ALTER TABLE ONLY public.accounts_boardmember
    ADD CONSTRAINT accounts_boardmember_user_id_f214d4c8_fk_accounts_ FOREIGN KEY (user_id) REFERENCES public.accounts_erasmususer(id) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.accounts_boardmember DROP CONSTRAINT accounts_boardmember_user_id_f214d4c8_fk_accounts_;
       public          postgres    false    243    237    3379            ~           2606    17151 G   accounts_coordinator accounts_coordinator_user_id_6fea830b_fk_accounts_    FK CONSTRAINT     �   ALTER TABLE ONLY public.accounts_coordinator
    ADD CONSTRAINT accounts_coordinator_user_id_6fea830b_fk_accounts_ FOREIGN KEY (user_id) REFERENCES public.accounts_erasmususer(id) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.accounts_coordinator DROP CONSTRAINT accounts_coordinator_user_id_6fea830b_fk_accounts_;
       public          postgres    false    237    3379    241            z           2606    17114 J   accounts_erasmususer accounts_erasmususer_user_id_e328830f_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.accounts_erasmususer
    ADD CONSTRAINT accounts_erasmususer_user_id_e328830f_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 t   ALTER TABLE ONLY public.accounts_erasmususer DROP CONSTRAINT accounts_erasmususer_user_id_e328830f_fk_auth_user_id;
       public          postgres    false    3362    231    237            {           2606    17211 F   accounts_student accounts_student_coordinator_id_fca0fe7e_fk_accounts_    FK CONSTRAINT     �   ALTER TABLE ONLY public.accounts_student
    ADD CONSTRAINT accounts_student_coordinator_id_fca0fe7e_fk_accounts_ FOREIGN KEY (coordinator_id) REFERENCES public.accounts_coordinator(id) DEFERRABLE INITIALLY DEFERRED;
 p   ALTER TABLE ONLY public.accounts_student DROP CONSTRAINT accounts_student_coordinator_id_fca0fe7e_fk_accounts_;
       public          postgres    false    3389    241    239            |           2606    17234 E   accounts_student accounts_student_university_id_3d025979_fk_courses_u    FK CONSTRAINT     �   ALTER TABLE ONLY public.accounts_student
    ADD CONSTRAINT accounts_student_university_id_3d025979_fk_courses_u FOREIGN KEY (university_id) REFERENCES public.courses_university(id) DEFERRABLE INITIALLY DEFERRED;
 o   ALTER TABLE ONLY public.accounts_student DROP CONSTRAINT accounts_student_university_id_3d025979_fk_courses_u;
       public          postgres    false    3337    239    219            }           2606    17146 M   accounts_student accounts_student_user_id_683c461a_fk_accounts_erasmususer_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.accounts_student
    ADD CONSTRAINT accounts_student_user_id_683c461a_fk_accounts_erasmususer_id FOREIGN KEY (user_id) REFERENCES public.accounts_erasmususer(id) DEFERRABLE INITIALLY DEFERRED;
 w   ALTER TABLE ONLY public.accounts_student DROP CONSTRAINT accounts_student_user_id_683c461a_fk_accounts_erasmususer_id;
       public          postgres    false    237    3379    239            �           2606    17197 G   accounts_todo accounts_todo_user_id_e49e7c03_fk_accounts_erasmususer_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.accounts_todo
    ADD CONSTRAINT accounts_todo_user_id_e49e7c03_fk_accounts_erasmususer_id FOREIGN KEY (user_id) REFERENCES public.accounts_erasmususer(id) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.accounts_todo DROP CONSTRAINT accounts_todo_user_id_e49e7c03_fk_accounts_erasmususer_id;
       public          postgres    false    247    3379    237            �           2606    17168 O   accounts_usercourse accounts_usercourse_course_id_aa6ceb08_fk_courses_course_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.accounts_usercourse
    ADD CONSTRAINT accounts_usercourse_course_id_aa6ceb08_fk_courses_course_id FOREIGN KEY (course_id) REFERENCES public.courses_course(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.accounts_usercourse DROP CONSTRAINT accounts_usercourse_course_id_aa6ceb08_fk_courses_course_id;
       public          postgres    false    245    3334    217            �           2606    17173 O   accounts_usercourse accounts_usercourse_user_id_1e7fd3bb_fk_accounts_student_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.accounts_usercourse
    ADD CONSTRAINT accounts_usercourse_user_id_1e7fd3bb_fk_accounts_student_id FOREIGN KEY (user_id) REFERENCES public.accounts_student(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.accounts_usercourse DROP CONSTRAINT accounts_usercourse_user_id_1e7fd3bb_fk_accounts_student_id;
       public          postgres    false    3384    245    239            t           2606    17069 O   auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm;
       public          postgres    false    225    3349    229            u           2606    17064 P   auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id;
       public          postgres    false    229    3354    227            s           2606    17055 E   auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 o   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co;
       public          postgres    false    225    3344    223            v           2606    17084 D   auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 n   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id;
       public          postgres    false    3354    233    227            w           2606    17079 B   auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id;
       public          postgres    false    3362    233    231            x           2606    17098 S   auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 }   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm;
       public          postgres    false    225    3349    235            y           2606    17093 V   auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id;
       public          postgres    false    235    231    3362            �           2606    17324 M   communication_notification communication_notifi_user_id_6611ccd5_fk_accounts_    FK CONSTRAINT     �   ALTER TABLE ONLY public.communication_notification
    ADD CONSTRAINT communication_notifi_user_id_6611ccd5_fk_accounts_ FOREIGN KEY (user_id) REFERENCES public.accounts_erasmususer(id) DEFERRABLE INITIALLY DEFERRED;
 w   ALTER TABLE ONLY public.communication_notification DROP CONSTRAINT communication_notifi_user_id_6611ccd5_fk_accounts_;
       public          postgres    false    257    237    3379            �           2606    17410 Q   communication_post communication_post_forum_id_216369dc_fk_communication_forum_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.communication_post
    ADD CONSTRAINT communication_post_forum_id_216369dc_fk_communication_forum_id FOREIGN KEY (forum_id) REFERENCES public.communication_forum(id) DEFERRABLE INITIALLY DEFERRED;
 {   ALTER TABLE ONLY public.communication_post DROP CONSTRAINT communication_post_forum_id_216369dc_fk_communication_forum_id;
       public          postgres    false    259    261    3424            �           2606    17362 Q   communication_post communication_post_user_id_22b39414_fk_accounts_erasmususer_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.communication_post
    ADD CONSTRAINT communication_post_user_id_22b39414_fk_accounts_erasmususer_id FOREIGN KEY (user_id) REFERENCES public.accounts_erasmususer(id) DEFERRABLE INITIALLY DEFERRED;
 {   ALTER TABLE ONLY public.communication_post DROP CONSTRAINT communication_post_user_id_22b39414_fk_accounts_erasmususer_id;
       public          postgres    false    237    3379    261            �           2606    17308 I   communication_question communication_questi_user_id_30f264db_fk_accounts_    FK CONSTRAINT     �   ALTER TABLE ONLY public.communication_question
    ADD CONSTRAINT communication_questi_user_id_30f264db_fk_accounts_ FOREIGN KEY (user_id) REFERENCES public.accounts_coordinator(id) DEFERRABLE INITIALLY DEFERRED;
 s   ALTER TABLE ONLY public.communication_question DROP CONSTRAINT communication_questi_user_id_30f264db_fk_accounts_;
       public          postgres    false    255    3389    241            �           2606    17303 U   communication_question communication_question_faq_id_4871d988_fk_communication_faq_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.communication_question
    ADD CONSTRAINT communication_question_faq_id_4871d988_fk_communication_faq_id FOREIGN KEY (faq_id) REFERENCES public.communication_faq(id) DEFERRABLE INITIALLY DEFERRED;
    ALTER TABLE ONLY public.communication_question DROP CONSTRAINT communication_question_faq_id_4871d988_fk_communication_faq_id;
       public          postgres    false    3413    253    255            �           2606    17369 I   communication_response communication_respon_post_id_b8ed270b_fk_communica    FK CONSTRAINT     �   ALTER TABLE ONLY public.communication_response
    ADD CONSTRAINT communication_respon_post_id_b8ed270b_fk_communica FOREIGN KEY (post_id) REFERENCES public.communication_post(id) DEFERRABLE INITIALLY DEFERRED;
 s   ALTER TABLE ONLY public.communication_response DROP CONSTRAINT communication_respon_post_id_b8ed270b_fk_communica;
       public          postgres    false    261    3427    263            �           2606    17374 I   communication_response communication_respon_user_id_e3b25a8f_fk_accounts_    FK CONSTRAINT     �   ALTER TABLE ONLY public.communication_response
    ADD CONSTRAINT communication_respon_user_id_e3b25a8f_fk_accounts_ FOREIGN KEY (user_id) REFERENCES public.accounts_erasmususer(id) DEFERRABLE INITIALLY DEFERRED;
 s   ALTER TABLE ONLY public.communication_response DROP CONSTRAINT communication_respon_user_id_e3b25a8f_fk_accounts_;
       public          postgres    false    263    3379    237            o           2606    17399 H   courses_course courses_course_bilkent_equivalent_i_d03581e2_fk_courses_b    FK CONSTRAINT     �   ALTER TABLE ONLY public.courses_course
    ADD CONSTRAINT courses_course_bilkent_equivalent_i_d03581e2_fk_courses_b FOREIGN KEY (bilkent_equivalent_id) REFERENCES public.courses_bilkentcourse(id) DEFERRABLE INITIALLY DEFERRED;
 r   ALTER TABLE ONLY public.courses_course DROP CONSTRAINT courses_course_bilkent_equivalent_i_d03581e2_fk_courses_b;
       public          postgres    false    266    3438    217            p           2606    16979 D   courses_course courses_course_merged_course_id_3eda05f5_fk_courses_m    FK CONSTRAINT     �   ALTER TABLE ONLY public.courses_course
    ADD CONSTRAINT courses_course_merged_course_id_3eda05f5_fk_courses_m FOREIGN KEY (merged_course_id) REFERENCES public.courses_mergedcourse(id) DEFERRABLE INITIALLY DEFERRED;
 n   ALTER TABLE ONLY public.courses_course DROP CONSTRAINT courses_course_merged_course_id_3eda05f5_fk_courses_m;
       public          postgres    false    217    221    3340            q           2606    16984 M   courses_course courses_course_university_id_65d105dd_fk_courses_university_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.courses_course
    ADD CONSTRAINT courses_course_university_id_65d105dd_fk_courses_university_id FOREIGN KEY (university_id) REFERENCES public.courses_university(id) DEFERRABLE INITIALLY DEFERRED;
 w   ALTER TABLE ONLY public.courses_course DROP CONSTRAINT courses_course_university_id_65d105dd_fk_courses_university_id;
       public          postgres    false    3337    219    217            �           2606    17224 I   courses_document courses_document_user_id_0942113d_fk_accounts_student_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.courses_document
    ADD CONSTRAINT courses_document_user_id_0942113d_fk_accounts_student_id FOREIGN KEY (user_id) REFERENCES public.accounts_student(id) DEFERRABLE INITIALLY DEFERRED;
 s   ALTER TABLE ONLY public.courses_document DROP CONSTRAINT courses_document_user_id_0942113d_fk_accounts_student_id;
       public          postgres    false    239    3384    249            r           2606    17405 T   courses_mergedcourse courses_mergedcourse_bilkent_equivalent_i_06d38cc6_fk_courses_b    FK CONSTRAINT     �   ALTER TABLE ONLY public.courses_mergedcourse
    ADD CONSTRAINT courses_mergedcourse_bilkent_equivalent_i_06d38cc6_fk_courses_b FOREIGN KEY (bilkent_equivalent_id) REFERENCES public.courses_bilkentcourse(id) DEFERRABLE INITIALLY DEFERRED;
 ~   ALTER TABLE ONLY public.courses_mergedcourse DROP CONSTRAINT courses_mergedcourse_bilkent_equivalent_i_06d38cc6_fk_courses_b;
       public          postgres    false    3438    221    266            �           2606    17250 G   django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co;
       public          postgres    false    3344    223    251            �           2606    17255 B   django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id;
       public          postgres    false    251    231    3362            8      x������ � �      6      x�3�4����� d      2   t   x�u�;�0 ��9EN`��H݊�N\�ŤV%q����Xy�;Ba[��b�G�g�E������.; ���������b~єUĲ&GY��8W�[:�u�>����j�?�ι7:>/      4   <   x�3�4ᴴ����,�L�QH����,�L�4B###] a�\P���*��4�=... �q�      <   �   x�]���0���S܎�uA��	���ˉ^�RH����O(�*!{���r��5D���������!��ɠ1��;SC�he�#�b���%�F�YC3�͜�̘�c�t��9DA��C'V�%��yHeY��|ko@��+�>c�9�      :   !   x�3���4�4.#��41���=... |�"      (      x������ � �      *      x������ � �      &   o  x�e�]r�0���)|������{���"��6F?���F#M7y�4����ֈ�����v;\�2N�(�u�;\%��n�{�81Gan�����qbN�|����(��b�O?N��UT��&�����mP�����)
��d�?�}�ˎ"4���/�u��\^Q���
�+*ӽ�E:�Ǭ����sq�i���J�X�V U��g���3�����M�e:,��Z���6���`I�u�xՊ|�brw�H&�̪�y�m/v�:r��ՙ1ʏa*/c!�DUFj�ro���a,t�qՙc�l�6�'�s�[;x@-Q���\=^׿��2gܑ�U3�����,�hQM�%isB
�%W�L:)N��h������l<���t�aa�M��9܂;R�r]�E�2��$�	b��˖���(c�Y�ED��p�S6��O�:�B��X�Y>?�}�2��4v'
b*�H� �*�H�?r"�(s�����v���\M��㪔W���+T1� ��yQδ%�-�ˣ(c'�����H�r{f��F<�����n�~�i.��0�߮&c��J��:*@�3�:���j����v�� �ݙ���*1����*2<��(3���=�_E[�:!cw&���%��� (
�<���I��~�q��Ѵ�@��N{4��ٸ�@���cX�E�{�����9>3*Jp|&D����r-�^r�q9>��ϸ���-�ǧz�'�5�_�0��x������'��mS��}80���`���-�'�z� ��0���Ul:t-E�t[K� �t]K� �x_K�~����h�b�Ym��}[�nA���A���/��з%�>D~�p��i��6      ,   ^  x�u�Yk�@���)����4;��
��UK��F
es��D�D7���P;���~n��]�(��A�Jl*%�5'��3��ϒ�o���n��nx��q	o�l4�=�&\4��é�z@xB]�H�ȠD�t��G���}��u�F{g�W�M��� �.NI��l�n��$<�x����=NE�E���?����!�i�b=T��1�1_�&]M~�X�-ڠSP%CW	hWt�~� .�[hw�(R��\���д&��v?����'��덙b�-Vfn�(���n�es���i��l}���a�'.���}_ފ�qz,gY���F�z~I�^�k�      .      x������ � �      0   �  x��ˑ#1ѳ`�Qů/���s��:���Ϫ���ٚ9�VΥ�s��<�9�^�'�m����!�2���%y�P>2���«�«|���
�Z�WS�WK�W[�WG�WW�WO��C��V�u���[��S��K��[��G��W��OoM�iM�Y�x3����MM��4���ěGo^M�������[��[���Zo�)|�ai᭭���޺Zx�i��������Ko�6ޞ�x;��{�[om�}�����;C�X��i�3u����;)�K������w�.��x׺x�t�n��ݩ�w�.�ݺx7�}�]]�������{��{�׿N�o��_+W��\S��Zz7��{����pn�.��=>*i0�p�= �{@�� ��K�ƥp'q��r"�������FN�6rB��S����]�i݅��]ȩ݅��9���� r!�xr�w!�yr�w#�z7r�w#�{7r�w#O����������9�����'r��D� <�� O�L�9�D^�D�����E��ف'r����%x!g
^�قr����5x!g^ț�r��ey!g��ل7rF፜Ux#g��م7r�፜ex#^}�ن��\䃜u� g>�هr⃜�� g">�وrF�|y�"_^�_͑/r�⋜��"g*�����?I�ljڶ      B      x������ � �      H      x�3�,�t�/*�5����� "��      F      x������ � �      J   X   x�3�4202�5"C#+#C+#K=c3KCsmcΐ���dCΐԊ���Q�i�i�e�������T�������/==��Jc���� ޅ      D      x������ � �      L      x������ � �      O   "   x�3�LMM�TNcNל���2��b���� �:�         T   x�3��L�K�)VH�KQ�,.I�-�4�,���L`���7ܘ3�(@�4NC�C L	��8SQ�)�*�hW� �>�      >   �   x���=k�@�Y��K����_[
Y�B���)��''�8vs���N�t0�$=�BX��=�W�پ�:p�?�e��'c]�>lm�{��%��ű�bAi'"�D�72��= 4��9aY�WW���m���k�aJ�
J��S�<��ݸ�Xn<��ޅ�����Zk3|�r��E5��FWhe�:���i���	)�f9}��9�O����I9�R�r"��;��      "      x�3�4�,�L�L����� Oy          +   x�3�tp��.�,�J-�I�K�4�4�4�L�t����� ��w      @   �  x����O�0���+��4j���_�����pB���F�ab����D6��I[�~��wo1����c�DF%��7#-M�ە-#�����͓,���34��Lf�Da��	��%(���H�.�2P�"�� ��)�ji��A�_��T�!�3B�A� $�:M�� ��h��T����h�x�|Vw΢����E'@���)_["Yv�;�8M΋�4U���ɤ,>l��3��$���2F3�8�(ۛ�U�]��˻�7�\�(���v)�sJP)��U�� �����S�?ғu��t��:��q֡E�I��Av~�sa��XĮ1�օ4�ۍ���ֿ�&��o��
__���@�� IJՙ�,��/LB3      $   �   x�]�Mr� ���0�@~�ܥl�i@�$2����x��!z�5#������Y�.p�`B�0���K¬p6~�0�d/�Hd�t,ZB���h$��Wb��x �!a����&�6`+k�XJ���k�ln���࣠� �qw�I�mM���b�%�=��L�`/;�(3��duR��NS5��j�菙�Sy�u}�������5;�<e�Ou�_��p���7���m��[K�i} ��䮭         u  x����n�8������b�Գ,@0�jג\J
���i�d��)4���H��s���8.a��!l7ts�./�P�7���FY���@�!��{�����㻷�=��:��`��l;��s�JP�xn��2t�>L���\�m`���{�������~���$D�u��3nf5��W@	&�j)_�2n�As-ԋ;����p���~Ѕ�Ӽ��_<��np����B���͇*M S&��4f�ɇ䶺!�%�!�[w�}��?Q���@t7@Av�1�m�\J��&ha.7)t�Ņ���ϧ�;����.?W��F�`��v��yۏ�s�xۺ�����JH^ ���M�2�m�T�Zg
��BL��mI�$��#�l���tv����ٻv<�y�+�#�8�m����Yx�E@�9/>/���f&7�[�ŏ3����k�srҟ�J�\�E ��$PT(�N�$ Vȡ�W��Ի(��}w��=��R��"S`K�Z�(߬����"ʙb�ꝙ����Q��0aھ��Iͥ �F�m���g\4|l��Z=Z׶u�����w�C��0w��=~�#ʭ
��V�zh.Y��/��Vi�YZS�z���ͦ��}7M릢�{��^�pƿ��Z�RN��b����]wy�1�D3�c�n���s�E[[
��!r��M���϶\�7�UR�at��-��҅����vu�o �$�[�w��]�<E�Pٽ�&w�M썐$�$�w���晗��H;�<x�k(cRgc�Ȃ�>����c�1G��1`���h�5�??2E����15�.碈�S�t,dAJ����stk�>+p�Dh�ɣ-�'�c�\??�U㷡��#�=1V ���1��8w��I`L�2�=�{��W0�t|�h)�u���l'H�	~�bdk�
�Z�4s�wcU��l�OϷ���8?%Ӎ@�d�1q��_���V�W �;�I��q��S��.u2+�cߺNEsulf��{�`,��g���UN y�LcJ�M2����Ĥ�'H�;�a�!ꠘH���poJ�82}:�2V
Z� ���7DY��J�����0��Q)�E9]ț}>#]����c��H�)FnPJ�u�7���FLl�˸�қ���o��r�Q���\��ʄ�iͮM�Q��a1�9I7�r��9���Ɓ�0�<�k#�ض��O����O�k�(�A|F+E��(9�,�/�d�v�o��T�F�/9d���w�����i��D8E1��2 I7-YN�f�����M:a��ۋ~�=�����q׸PC��Zy��E�CɎ<�.�ҭ�};Ovs������,Յ(4�N�������Ω�jn>����pmB��5 ��3�#�������`�      M   
  x���n�0  г|��
-���8@���,1B�V�~���`IQ�n���$j�B=��b\��dV�ϼW����.���\mh�82��˩X_��¢��=M5���\����Oa%�@����u��<��X��V��:.�m���z?N����~�;�[|�Ŏa��gr?���$��Ѽ IR��"߼l�N?^Zx4����&��2�J���\����"�6ddD��S��؇�l��	P�>U��o@��ek��24��类��E� ^C     